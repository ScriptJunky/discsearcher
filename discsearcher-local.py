import re
import sys
import pandas as pd
import argparse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

parser = argparse.ArgumentParser()
parser.add_argument('--mfgr', action='append', help='Manufacturer of the disc')
parser.add_argument('--name', action='append', help='Disc model or name')
parser.add_argument('--type', action='append', help='Type of disc')
parser.add_argument('--speed', action='append', help='Speed rating')
parser.add_argument('--glide', action='append', help='Glide')
parser.add_argument('--turn', action='append', help='Turn (prefix with negative supported)')
parser.add_argument('--fade', action='append', help='Fade')
parser.add_argument('--full', action='store_true', help='Print full contents of CSV file')
args = parser.parse_args()

csv = pd.read_csv('discs.csv', header=0, delimiter=',')

namefilters = []
typefilters = []
speedfilters = []
glidefilters = []
turnfilters = []
fadefilters = []

finalfilter = []

if args.full:
    print(csv)
    sys.exit(0)

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

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
