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

WILDCARD is NOT supported.
=======================================================================================================================================================================

EXAMPLE:
=======================================================================================================================================================================
➜~/git/discsearcher(master✗)» python3 discsearcher-local.py --mfgrrx '(MVP|Axiom Discs|Streamline Discs)' --type Distance --speedrx '(10|11|12)' --turnrx '^-[1-4]'                                                                                       [13:15:33]
         Name      Manufacturer      Type  Speed  Glide  Turn  Fade
324   Impulse               MVP  Distance     10      5    -3   1.0
326   Inertia               MVP  Distance     10      5    -2   2.0
327  Insanity       Axiom Discs  Distance     10      5    -2   1.0
482   Orbital               MVP  Distance     12      5    -4   1.0
522    Photon               MVP  Distance     12      5    -1   3.0
726     Tesla               MVP  Distance     10      5    -1   2.0
747     Trace  Streamline Discs  Distance     11      5    -1   2.0
770    Vanish       Axiom Discs  Distance     12      5    -3   2.0
783     Virus       Axiom Discs  Distance     10      5    -3   1.0
803      Wave               MVP  Distance     11      5    -2   2.0
819     Wrath       Axiom Discs  Distance     10      4    -1   2.0
➜~/git/discsearcher(master✗)»
========================================================================================================================================================================
'''

parser = argparse.ArgumentParser(description=regexaddendum, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--full', action='store_true', help='Show details for all known discs.')
parser.add_argument('--manufacturers', action='store_true', help='provide list of all known disc manufacturers.')
parser.add_argument('--discnames', action='store_true', help='provide list of all known disc names.')
parser.add_argument('--mfgr', action='append', help='Filter discs on manufacturer.')
parser.add_argument('--name', action='append', help='Filter discs by name.')
parser.add_argument('--type', action='append', help='Filter discs by type (Distance, Fairway, Midrange, or Putter).')
parser.add_argument('--speed', action='append', help='Filter discs by speed.')
parser.add_argument('--glide', action='append', help='Filter discs by glide.')
parser.add_argument('--turn', action='append', help='Filter discs by turn -- (Prepend value with "-").')
parser.add_argument('--fade', action='append', help='Filter discs by fade.')
parser.add_argument('--mfgrrx', help='Use regex to filter discs by manufacturer.')
parser.add_argument('--namerx', help='Use regex to filter discs by name.')
parser.add_argument('--typerx', help='Use regex to filter discs by type.')
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

if args.typerx:
    args.typerx = list(exrex.generate(fr'{args.typerx}'))
    typerxfilters = f'csv.Type.isin({args.typerx})'
    finalfilter.append(typerxfilters)

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

if args.type:
    typefilters = f'csv.Type.isin({args.type})'
    finalfilter.append(typefilters)

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
