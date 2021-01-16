import argparse
import exrex
import hashlib
import os
import pandas as pd
import re
import requests
import socket
import sys
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from tabulate import tabulate

# Adding in some retry w/ backoff logic. Helps with slower chans.
session = requests.Session()
retry = Retry(connect=5, backoff_factor=3)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Setting socket level timeout
socket.setdefaulttimeout(300)

# Version Information
contact = 'discsearcher@icloud.com'
vnum = 2021.016
version = f'''
discsearcher v{vnum}
\u00A9 2020 - Throw The Roller, LLC.
{contact}
'''

updateissue='''
An error occurred in obtaining an updated list of discs.
Please try running the tool again!
'''

updatesuccess='''
discs.csv was successfully updated!
Searching will be successful on next run.
'''

regexaddendum=f'''
STANDARD FLAGS:
--full           Print the full listing of discs (and their flight numbers) that Infinite Discs sells.
--manufacturers  Print a list of all disc manufacturers available from Infinite Discs.
--discnames      Print the list of disc names available from Infinite Discs.
--update         Update the local csv file that stores discs, their manufacturers, and their flight numbers.
--version        Print version and exit.

FILTERING (STANDARD FILTERS):
--mfgr         Used to include discs by manufacturer                                      (--mfgr Innova, for example)
--name         Used to include discs specifically by name                                 (--name Mamba, for example)
--speed        Used to include discs with a specific speed                                (--speed 10, for example. Will only show 10.0 and not 10.1 - 10.9)
--glide        Used to include discs with a specific glide                                (--glide 5, for example. Will only show 5.0 and not 5.1 - 5.9)
--turn         Used to include discs with a specific turn                                 (--turn -5, for example. Will only show -5.0 and not -5.1 - -5.9)
--fade         Used to include discs with a specific fade                                 (--fade 3, for example. Will only show 3.0 and not 3.1 - 3.9)
--diam         Used to include discs with a specific diameter                             (--diam 21.5, for example. Will only show discs that have a diameter of 21.5cm)
--height       Used to include discs with a specific height                               (--height 1.7, for example. Will only show discs that have a height of 1.7cm)
--depth        Used to include discs with a specific rim depth                            (--depth 1.4, for example. Will only show discs that have a rim depth of 1.4cm)
--width        Used to include discs with a specific rim width                            (--width 1.5, for example. Will only show discs that have a rim width of 1.5cm)

FILTERING (REGULAR EXPRESSIONS):
--mfgrrx       Used to search for multiple manufacturers by name, with a single call      (--mfgrrx '(MVP|Axiom|Streamline)', for example. Only discs made by MVP, Axiom, or Streamline will be matched.)
--namerx       Used to search for multiple discs by name, with a single call              (--namerx '(Wave|Wraith|Aries)', for example. Only the Wave, Wraith, and Aries will be matched.)
--speedrx      Used to search for multiple speeds and speed ranges, with a single call    (--speedrx '(10|11)\.[0-9]', for example. Speed between 10.0-11.9 will be matched.)
--gliderx      Used to search for multiple glides and glide ranges, with a single call    (--gliderx '[56]\.[0-9]', for example. Glide between 5.0-6.9 will be matched.)
--turnrx       Used to search for multiple turn and turn ranges, with a single call       (--turnrx '^-[3-5]\.[0-9]', for example. Turn ratings between -3.0 and -5.9 will be matched.)
--faderx       Used to search for multiple fade and fade ranges, with a single call       (--faderx '^-[2-3]\.[0-9]', for example. Fade ratings between -2.0 and -3.9 will be matched.)
--diamrx       Used to search for multiple diams and diam ranges, with a single call      (--diamrx '(20|21)\.\d', for example. Diameter between 20.0-21.9 will be matched.)
--heightrx     Used to search for multiple heights and height ranges, with a single call  (--heightrx '1\.[0-9]', for example. Heights between 1.0-1.9 will be matched.)
--depthrx      Used to search for multiple depth and depth ranges, with a single call     (--depthrx '1\.[0-9]', for example. Rim Depths between 1.0 and 1.9 will be matched.)
--widthrx      Used to search for multiple width and width ranges, with a single call     (--widthrx '1\.[0-9]', for example. Rim Widths between 1.0 and 1.9 will be matched.)

*******ALL FILTERING FLAGS CAN BE COMPOUNDED, AS WELL AS MIXED\MATCHED TOGETHER IN A SINGLE QUERY*******
'''

parser = argparse.ArgumentParser(description=regexaddendum, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--version', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--full', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--manufacturers', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--discnames', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--update', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--mfgr', action='append', help=argparse.SUPPRESS)
parser.add_argument('--name', action='append', help=argparse.SUPPRESS)
parser.add_argument('--speed', action='append', help=argparse.SUPPRESS)
parser.add_argument('--glide', action='append', help=argparse.SUPPRESS)
parser.add_argument('--turn', action='append', help=argparse.SUPPRESS)
parser.add_argument('--fade', action='append', help=argparse.SUPPRESS)
parser.add_argument('--diam', action='append', help=argparse.SUPPRESS)
parser.add_argument('--height', action='append', help=argparse.SUPPRESS)
parser.add_argument('--depth', action='append', help=argparse.SUPPRESS)
parser.add_argument('--width', action='append', help=argparse.SUPPRESS)
parser.add_argument('--mfgrrx', help=argparse.SUPPRESS)
parser.add_argument('--namerx', help=argparse.SUPPRESS)
parser.add_argument('--speedrx', help=argparse.SUPPRESS)
parser.add_argument('--gliderx', help=argparse.SUPPRESS)
parser.add_argument('--turnrx', help=argparse.SUPPRESS)
parser.add_argument('--faderx', help=argparse.SUPPRESS)
parser.add_argument('--diamrx', help=argparse.SUPPRESS)
parser.add_argument('--heightrx', help=argparse.SUPPRESS)
parser.add_argument('--depthrx', help=argparse.SUPPRESS)
parser.add_argument('--widthrx', help=argparse.SUPPRESS)
args = parser.parse_args()

if args.version:
    print(version)
    sys.exit(0)

if not os.path.exists('discs.csv'):
    print('The discs.csv file is missing! Downloading the latest copy....')
    try:
        csvdata = requests.get('https://bitbucket.org/biscuits/discsearcher/downloads/discs.csv').text
        csvfile = open('discs.csv', 'w')
        csvfile.write(csvdata)
        csvfile.close()
    except:
        print(updateissue)
        sys.exit(1)
    print(updatesuccess)
    sys.exit(0)
else:
    print('Checking for a new version of the discs.csv file....')
    with open('discs.csv', 'rb') as csvfile:
        localcsv = csvfile.read()
        localhash = hashlib.md5(localcsv)
    remotecsvfile = requests.get('https://bitbucket.org/biscuits/discsearcher/downloads/discs.csv').text
    remoteread = remotecsvfile.encode('ascii')
    remotehash = hashlib.md5(remoteread)
    if localhash.hexdigest() != remotehash.hexdigest():
        print('Updating the local CSV file to current....')
        os.remove('discs.csv')
        csvcreate = open('discs.csv', 'w')
        csvcreate.write(remotecsvfile)
        csvcreate.close()
        print(updatesuccess)
        sys.exit(0)

if time.time()-os.path.getctime('discs.csv') > 2629743:
    print('The discs.csv file is more than 30 days old! Downloading the latest copy....')
    try:
        os.remove('discs.csv')
        csvdata = requests.get('https://bitbucket.org/biscuits/discsearcher/downloads/discs.csv').text
        csvfile = open('discs.csv', 'w')
        csvfile.write(csvdata)
        csvfile.close()
    except:
        print(updateissue)
        sys.exit(1)
    print(updatesuccess)
    sys.exit(0)

if args.update:
    print('The discs.csv file will now be updated......')
    try:
        os.remove('discs.csv')
        csvdata = requests.get('https://bitbucket.org/biscuits/discsearcher/downloads/discs.csv').text
        csvfile = open('discs.csv', 'w')
        csvfile.write(csvdata)
        csvfile.close()
    except:
        print(updateissue)
        sys.exit(1)
    print(updatesuccess)
    sys.exit(0)



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

csv = pd.read_csv('discs.csv', header=0,  delimiter=',')

if args.full:
    print(csv)
    sys.exit(0)

if args.manufacturers:
    manufacturer_list = csv['Manufacturer'].unique()
    manufacturer_list.sort()
    print(*manufacturer_list, sep='\n')
    sys.exit(0)

if args.discnames:
    discnames_list = csv['Name'].unique()
    discnames_list.sort()
    print(*discnames_list, sep='\n')
    sys.exit(0)

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)


mfgrfilters = []
namefilters = []
typefilters = []
speedfilters = []
glidefilters = []
turnfilters = []
fadefilters = []
diamfilters = []
heightfilters = []
depthfilters = []
widthfilters = []

mfgrrxfilters = []
namerxfilters = []
typerxfilters = []
speedrxfilters = []
gliderxfilters = []
turnrxfilters = []
faderxfilters = []
diamrxfilters = []
heightrxfilters = []
depthrxfilters = []
widthrxfilters = []

finalfilter = []

if args.mfgr:
    mfgrfilters = f'csv.Manufacturer.isin({args.mfgr})'
    finalfilter.append(mfgrfilters)

if args.name:
    namefilters = f'csv.Name.isin({args.name})'
    finalfilter.append(namefilters)

if args.speed:
    speedfilters = f'csv.Speed.isin({args.speed})'
    speedfilters = re.sub(r"'", r"", speedfilters)
    finalfilter.append(speedfilters)

if args.glide:
    glidefilters = f'csv.Glide.isin({args.glide})'
    glidefilters = re.sub(r"'", r"", glidefilters)
    finalfilter.append(glidefilters)

if args.turn:
    turnfilters = f'csv.Turn.isin({args.turn})'
    turnfilters = re.sub(r"'", r"", turnfilters)
    finalfilter.append(turnfilters)

if args.fade:
    fadefilters = f'csv.Fade.isin({args.fade})'
    fadefilters = re.sub(r"'", r"", fadefilters)
    finalfilter.append(fadefilters)

if args.diam:
    diamfilters = f'csv.Diameter.isin({args.diam})'
    diamfilters = re.sub(r"'", r"", diamfilters)
    finalfilter.append(diamfilters)

if args.height:
    heightfilters = f'csv.Height.isin({args.height})'
    heightfilters = re.sub(r"'", r"", heightfilters)
    finalfilter.append(heightfilters)

if args.depth:
    depthfilters = f'csv.RimDepth.isin({args.depth})'
    depthfilters = re.sub(r"'", r"", depthfilters)
    finalfilter.append(depthfilters)

if args.width:
    widthfilters = f'csv.RimWidth.isin({args.width})'
    widthfilters = re.sub(r"'", r"", widthfilters)
    finalfilter.append(widthfilters)

if args.mfgrrx:
    args.mfgrrx = list(exrex.generate(fr'{args.mfgrrx}'))
    mfgrrxfilters = f'csv.Manufacturer.isin({args.mfgrrx})'
    finalfilter.append(mfgrrxfilters)

if args.namerx:
    args.namerx = list(exrex.generate(fr'{args.namerx}'))
    namerxfilters = f'csv.Name.isin({args.namerx})'
    finalfilter.append(namerxfilters)

if args.speedrx:
    args.speedrx = list(exrex.generate(fr'{args.speedrx}'))
    speedrxfilters = f'csv.Speed.isin({args.speedrx})'
    speedrxfilters = re.sub(r"'", r"", speedrxfilters)
    finalfilter.append(speedrxfilters)

if args.gliderx:
    args.gliderx = list(exrex.generate(fr'{args.gliderx}'))
    gliderxfilters = f'csv.Glide.isin({args.gliderx})'
    gliderxfilters = re.sub(r"'", r"", gliderxfilters)
    finalfilter.append(gliderxfilters)

if args.turnrx:
    args.turnrx = list(exrex.generate(fr'{args.turnrx}'))
    turnrxfilters = f'csv.Turn.isin({args.turnrx})'
    turnrxfilters = re.sub(r"'", r"", turnrxfilters)
    finalfilter.append(turnrxfilters)

if args.faderx:
    args.faderx = list(exrex.generate(fr'{args.faderx}'))
    faderxfilters = f'csv.Fade.isin({args.faderx})'
    faderxfilters = re.sub(r"'", r"", faderxfilters)
    finalfilter.append(faderxfilters)

if args.diamrx:
    args.diamrx = list(exrex.generate(fr'{args.diamrx}'))
    diamrxfilters = f'csv.Diameter.isin({args.diamrx})'
    diamrxfilters = re.sub(r"'", r"", diamrxfilters)
    finalfilter.append(diamrxfilters)

if args.heightrx:
    args.heightrx = list(exrex.generate(fr'{args.heightrx}'))
    heightrxfilters = f'csv.Height.isin({args.heightrx})'
    heightrxfilters = re.sub(r"'", r"", heightrxfilters)
    finalfilter.append(heightrxfilters)

if args.depthrx:
    args.depthrx = list(exrex.generate(fr'{args.depthrx}'))
    depthrxfilters = f'csv.RimDepth.isin({args.depthrx})'
    depthrxfilters = re.sub(r"'", r"", depthrxfilters)
    finalfilter.append(depthrxfilters)

if args.widthrx:
    args.widthrx = list(exrex.generate(fr'{args.widthrx}'))
    widthrxfilters = f'csv.RimWidth.isin({args.widthrx})'
    widthrxfilters = re.sub(r"'", r"", widthrxfilters)
    finalfilter.append(widthrxfilters)

finalfilter = ' & '.join(finalfilter)

newcsv = 'print(tabulate(csv[' + finalfilter + '], disable_numparse=True, showindex=False, headers=csv.columns))'

exec(newcsv)
