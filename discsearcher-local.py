import re
import sys
import exrex
import pandas as pd
import argparse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

regexaddendum='''
REGEX USAGE:
=======================================================================================================================================================================
When using regex, the following style is acceptable:

^[1-9]:        Match all values beginning with '-' and the second character is between 1 and 9.
(Buzzz|Manta): Match both the Buzzz and Manta discs.

WILDCARD is NOT supported, and literal '.' characters MUST be escaped!
=======================================================================================================================================================================

EXAMPLE:
=======================================================================================================================================================================
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --mfgrrx '^(MVP|Axiom|Streamline)' --speedrx '(10|11|12)\.[0-9]' --turnrx '^-[1-4]\.[0-9]'
    Manufacturer     Name  Speed  Glide  Turn  Fade
18         Axiom   Vanish   11.5    5.0  -2.7   1.9
617          MVP  Impulse   10.0    4.9  -2.9   1.1
618          MVP  Inertia   10.3    4.9  -1.9   2.0
623          MVP  Orbital   11.5    5.0  -4.4   0.9
625          MVP   Photon   11.5    4.9  -1.0   2.7
629          MVP     Wave   11.4    5.1  -1.9   1.8
767   Streamline    Trace   11.0    5.0  -1.0   2.0
➜~/git/discsearcher(master✗)»
========================================================================================================================================================================
'''

parser = argparse.ArgumentParser(description=regexaddendum, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--full', action='store_true', help='Show details for all known discs.')
parser.add_argument('--manufacturers', action='store_true', help='provide list of all known disc manufacturers.')
parser.add_argument('--discnames', action='store_true', help='provide list of all known disc names.')
parser.add_argument('--mfgr', action='append', help='Filter discs on manufacturer.')
parser.add_argument('--name', action='append', help='Filter discs by name.')
parser.add_argument('--speed', action='append', help='Filter discs by speed.')
parser.add_argument('--glide', action='append', help='Filter discs by glide.')
parser.add_argument('--turn', action='append', help='Filter discs by turn -- (Prepend value with "-").')
parser.add_argument('--fade', action='append', help='Filter discs by fade.')
parser.add_argument('--mfgrrx', help='Use regex to filter discs by manufacturer.')
parser.add_argument('--namerx', help='Use regex to filter discs by name.')
parser.add_argument('--speedrx', help='Use regex to filter discs by speed.')
parser.add_argument('--gliderx', help='Use regex to filter discs by glide.')
parser.add_argument('--turnrx', help='Use regex to filter discs by turn.')
parser.add_argument('--faderx', help='Use regex to filter discs by fade.')
args = parser.parse_args()

csv = pd.read_csv('discs.csv', header=0, delimiter=',')

if args.full:
    print(csv)
    sys.exit(0)

if args.manufacturers:
    manufacturer_list = csv['Manufacturer'].unique()
    manufacturer_list.sort()
    for m in manufacturer_list:
        print(m)
    sys.exit(0)

if args.discnames:
    discnames_list = csv['Name'].unique()
    discnames_list.sort()
    for dn in discnames_list:
        print(dn)
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

newcsv = 'print(csv[' + finalfilter + '])'

exec(newcsv)
