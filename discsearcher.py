import argparse
import exrex
import numpy as np
import os
import pandas as pd
import re
import requests
import socket
import sys
import time
from bs4 import BeautifulSoup as soup
from tabulate import tabulate

socket.setdefaulttimeout(300)

contact = 'discsearcher@icloud.com'
vnum = 2020.364

version = f'''
discsearcher v{vnum}
\u00A9 2020 - Throw The Roller, LLC.
{contact}
'''

url = 'https://infinitediscs.com'
referral = '?tag=3c8c6529'

def csvgenerator():
    mfgrs = []
    mfgrnames = []

    mainpage = requests.get(url).text
    soupf = soup(mainpage, 'lxml')

    for i in soupf.find_all('a', attrs={'href': re.compile("/category/")}):
        mfgrs.append(i)

    for m in mfgrs:
        m = str(m).split('"')
        mfgrnames.append(m[1])

    mfgrnames = np.unique(mfgrnames)

    df = pd.DataFrame(columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'Rim Depth', 'Rim Width'])

    for i in mfgrnames:
        idurl = requests.get(url + i).text
        soupf = soup(idurl, 'lxml')
        fixeditems = re.sub(r'\r\n.*pull-left', r'', str(soupf.find_all('h4')))
        fixeditems2 = fixeditems.split(',')
        fixeditems2 = [o for o in fixeditems2 if re.search('</small></h4>', o)]
        fixeditems2 = [re.sub('"><small>', ',', o) for o in fixeditems2]
        fixeditems2 = [re.sub('</small></h4>', '', o) for o in fixeditems2]
        fixeditems2 = [re.sub(r'<h4>\s+', '', o) for o in fixeditems2]
        fixeditems2 = [re.sub('/', ',', o) for o in fixeditems2]
        fixeditems2 = [re.sub(r'^\s+', '', o) for o in fixeditems2]
        for each in fixeditems2:
            each = f'{i.replace("/category/", "")},{each}'
            each = list(each.split(','))
            each[2] = float(each[2].replace("'", ""))
            each[3] = float(each[3].replace("'", ""))
            each[4] = float(each[4].replace("'", ""))
            each[5] = float(each[5].replace("'", ""))
            print(each)
            if each[1] == 'CD':
                each[1] = 'CD-Craze'
            if each[1] == 'DD':
                each[1] = 'DD-Hysteria'
            if each[1] == 'DD2':
                each[1] = 'DD2-Frenzy'
            if each[1] == 'DD3 ':
                each[1] = 'DD3'
            if each[1] == 'Enigma':
                each[1] = 'Evolution-Enigma'
            if each[1] == 'PD':
                each[1] = 'PD-Freak'
            if each[1] == 'PD2':
                each[1] = 'PD2-Chaos'
            if each[1] == 'TD':
                each[1] = 'TD-Rush'
            if each[1] == 'MD2':
                each[1] = 'MD2-Fiend'
            if each[1] == 'FL':
                each[1] = 'Firebird-FL'
            if each[1] == 'KC Aviar':
                each[1] = 'Aviar-KC-Pro'
            if each[1] == 'TeeBird +':
                each[1] = 'TeeBird-'
            if each[1] == 'Roc +':
                each[1] = 'Roc-'
            if each[1] == 'XD +':
                each[1] = 'XD-'
            if each[1] == 'Luan':
                each[1] = 'Lu'
            if each[1] == 'Claws':
                each[1] = 'Talon-(Claws)'
            if each[1] == 'D Model US+':
                each[1] = 'D-Model-US-Plus'
            name = re.sub(r' ', '-', each[1])
            name = re.sub(r"'", '', name)
            name = re.sub(r'\+$', '-', name)
            dimurl = url + '/' + each[0] + '-' + name
            discpage = requests.get(dimurl).text
            print(name, dimurl)
            soupf = soup(discpage, 'lxml')
            diameter = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblDiameter'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
            each.append(diameter)
            height = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblHeight'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
            each.append(height)
            rimdepth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimDepth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
            each.append(rimdepth)
            rimwidth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimWidth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
            each.append(rimwidth)
            print(each)
            df = df.append(pd.DataFrame([each], columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'Rim Depth', 'Rim Width']), ignore_index=True)

    df['Purchase Url'] = url + '/' + df['Manufacturer'] + '-' + df['Name'].replace(regex={r' ': '-', r"'": '', r'\+': ''}) + referral

    df.to_csv('discs.csv', index=False)

updateissue='''
An error occurred in obtaining an updated list of discs.
Please try running the tool again!
'''

regexaddendum=f'''
STANDARD FLAGS:
--full           Print the full listing of discs (and their flight numbers) that Infinite Discs sells.
--manufacturers  Print a list of all disc manufacturers available from Infinite Discs.
--discnames      Print the list of disc names available from Infinite Discs.
--update         Update the local csv file that stores discs, their manufacturers, and their flight numbers.
--version        Print version and exit.

FILTERING (STANDARD FILTERS):
--mfgr           Used to include specific manufacturers in the search output        (--mfgr Innova, for example)
--name           Used to include specific discs in the search output                (--name Mamba, for example)
--speed          Used to include discs with a specific speed in the search output   (--speed 10, for example. Will only show 10.0 and not 10.1 - 10.9)
--glide          Used to include discs with a specific glide in the search output   (--glide 5, for example. Will only show 5.0 and not 5.1 - 5.9)
--turn           Used to include discs with a specific turn in the search output    (--turn -5, for example. Will only show -5.0 and not -5.1 - -5.9)
--fade           Used to include discs with a specific fade in the search output    (--fade 3, for example. Will only show 3.0 and not 3.1 - 3.9)

FILTERING (REGULAR EXPRESSIONS):
--mfgrrx         This can be used to search for multiple manufacturers by name, with a single call    (--mfgrrx '(MVP|Axiom|Streamline)', for example. Only discs made by MVP, Axiom, or Streamline will be matched.)
--namerx         This can be used to search for multiple discs by name, with a single call            (--namerx '(Wave|Wraith|Aries)', for example. Only the Wave, Wraith, and Aries will be matched.)
--speedrx        This can be used to search for multiple speeds and speed ranges, with a single call  (--speedrx '(10|11)\.[0-9]', for example. Speed between 10.0-11.9 will be matched.)
--gliderx        This can be used to search for multiple glides and glide ranges, with a single call  (--gliderx '[56]\.[0-9]', for example. Glide between 5.0-6.9 will be matched.)
--turnrx         This can be used to search for multiple turn and turn ranges, with a single call     (--turnrx '^-[3-5]\.[0-9]', for example. Turn ratings between -3.0 and -5.9 will be matched.)
--faderx         This can be used to search for multiple fade and fade ranges, with a single call     (--faderx '^-[2-3]\.[0-9]', for example. Fade ratings between -2.0 and -3.9 will be matched.)

EXAMPLES:

================================================================================================================================
Filtering - Standard Filters
================================================================================================================================
~/git/discsearcher(master)» discsearcher --turn -2 --speed 11
Manufacturer    Name     Speed    Glide    Turn    Fade    Purchase Url
--------------  -------  -------  -------  ------  ------  -------------------------------------------------------
Discraft        Wildcat  11.0     5.0      -2.0    3.0     https://infinitediscs.com/Discraft-Wildcat?tag=3c8c6529
Salient         Napalm   11.0     5.0      -2.0    2.0     https://infinitediscs.com/Salient-Napalm?tag=3c8c6529
~/git/discsearcher(master)»

================================================================================================================================
Filtering - Regular Expressions
================================================================================================================================
~/git/discsearcher(master)» discsearcher --turnrx '^-2\.[0-9]' --speedrx '11\.[0-9]'
Manufacturer    Name      Speed    Glide    Turn    Fade    Purchase Url
--------------  --------  -------  -------  ------  ------  -------------------------------------------------------------
Axiom           Vanish    11.5     5.0      -2.7    1.9     https://infinitediscs.com/Axiom-Vanish?tag=3c8c6529
Discraft        Spectra   11.8     4.9      -2.0    2.0     https://infinitediscs.com/Discraft-Spectra?tag=3c8c6529
Discraft        Thrasher  11.9     5.1      -2.8    1.9     https://infinitediscs.com/Discraft-Thrasher?tag=3c8c6529
Discraft        Wildcat   11.0     5.0      -2.0    3.0     https://infinitediscs.com/Discraft-Wildcat?tag=3c8c6529
Dynamic-Discs   Renegade  11.0     5.0      -2.1    2.6     https://infinitediscs.com/Dynamic-Discs-Renegade?tag=3c8c6529
Infinite-Discs  Maya      11.9     5.1      -2.9    1.0     https://infinitediscs.com/Infinite-Discs-Maya?tag=3c8c6529
Innova          Mystere   11.0     6.0      -2.2    1.9     https://infinitediscs.com/Innova-Mystere?tag=3c8c6529
Innova          Wahoo     11.9     6.0      -2.1    2.0     https://infinitediscs.com/Innova-Wahoo?tag=3c8c6529
Millennium      Aries     11.0     6.0      -2.6    1.1     https://infinitediscs.com/Millennium-Aries?tag=3c8c6529
Salient         Napalm    11.0     5.0      -2.0    2.0     https://infinitediscs.com/Salient-Napalm?tag=3c8c6529
~/git/discsearcher(master)»

NOTE: You should know the escape character of your OS prior to using regular expression searches.
NOTE: The common wildcard characters (*|.) are NOT supported, and can cause the tool to fail or crash.

MacOS escape:   {chr(92)}
Linux escape:   {chr(92)}
Windows escape: ^

================================================================================================================================
Filtering - Compound Query
================================================================================================================================
~/git/discsearcher(master)» python3 discsearcher.py --turnrx '^-2\.[0-9]' --speedrx '11\.[0-9]' --mfgr Innova --mfgr Discraft
\Manufacturer    Name      Speed    Glide    Turn    Fade    Purchase Url
--------------  --------  -------  -------  ------  ------  --------------------------------------------------------
Discraft        Spectra   11.8     4.9      -2.0    2.0     https://infinitediscs.com/Discraft-Spectra?tag=3c8c6529
Discraft        Thrasher  11.9     5.1      -2.8    1.9     https://infinitediscs.com/Discraft-Thrasher?tag=3c8c6529
Discraft        Wildcat   11.0     5.0      -2.0    3.0     https://infinitediscs.com/Discraft-Wildcat?tag=3c8c6529
Innova          Mystere   11.0     6.0      -2.2    1.9     https://infinitediscs.com/Innova-Mystere?tag=3c8c6529
Innova          Wahoo     11.9     6.0      -2.1    2.0     https://infinitediscs.com/Innova-Wahoo?tag=3c8c6529
~/git/discsearcher(master)»
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
parser.add_argument('--mfgrrx', help=argparse.SUPPRESS)
parser.add_argument('--namerx', help=argparse.SUPPRESS)
parser.add_argument('--speedrx', help=argparse.SUPPRESS)
parser.add_argument('--gliderx', help=argparse.SUPPRESS)
parser.add_argument('--turnrx', help=argparse.SUPPRESS)
parser.add_argument('--faderx', help=argparse.SUPPRESS)
args = parser.parse_args()

if args.version:
    print(version)
    sys.exit(0)

csvgenerator()

#if not os.path.exists('discs.csv'):
#    print('The discs.csv file is missing! Generating a new copy......')
#    try:
#        csvgenerator()
#    except:
#        print(updateissue)
#        sys.exit(1)
#    sys.exit(0)

if time.time()-os.path.getctime('discs.csv') > 2629743:
    print('The discs.csv file is more than 30 days old! Generating a new copy......')
    try:
        csvgenerator()
    except:
        print(updateissue)
        sys.exit(1)
    sys.exit(0)

if args.update:
    print('The discs.csv file will now be updated......')
    try:
        csvgenerator()
    except:
        print(updateissue)
        sys.exit(1)
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

mfgrrxfilters = []
namerxfilters = []
typerxfilters = []
speedrxfilters = []
gliderxfilters = []
turnrxfilters = []
faderxfilters = []

finalfilter = []

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

finalfilter = ' & '.join(finalfilter)

newcsv = 'print(tabulate(csv[' + finalfilter + '], disable_numparse=True, showindex=False, headers=csv.columns))'

exec(newcsv)
