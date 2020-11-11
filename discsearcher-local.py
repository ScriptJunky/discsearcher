import sys
import pandas as pd
import argparse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

parser = argparse.ArgumentParser()
parser.add_argument('--mfgr', help='Manufacturer of the disc')
parser.add_argument('--name', help='Disc model or name')
parser.add_argument('--type', help='Type of disc')
parser.add_argument('--speed', help='Speed rating')
parser.add_argument('--glide', help='Glide')
parser.add_argument('--turn', help='Turn (prefix with negative supported)')
parser.add_argument('--fade', help='Fade')
parser.add_argument('--full', action='store_true', help='Print full contents of CSV file')
args = parser.parse_args()

csv = pd.read_csv('discs.csv', header=0, delimiter=',')

filters = []

if args.full:
    print(csv)
    sys.exit(0)

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.mfgr: 
    filters.append('(csv.Manufacturer == ' + "'" + args.mfgr + "'" + ')')

if args.name:
    filters.append('(csv.Name == ' + "'" + args.name + "'" + ')')

if args.type:
    filters.append('(csv.Type == ' + "'" + args.type + "'" + ')')

if args.speed:
    filters.append('(csv.Speed == ' + args.speed + ')')

if args.glide:
    filters.append('(csv.Glide == ' + args.glide + ')')

if args.turn:
    filters.append('(csv.Turn == ' + args.turn + ')')

if args.fade:
    filters.append('(csv.Fade == ' + args.fade + ')')

finalargs = " & ".join(filters)
newcsv = 'print(csv[' + finalargs + '])'

exec(newcsv)
