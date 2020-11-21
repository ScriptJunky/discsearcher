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

mfgrfilters = []
namefilters = []
typefilters = []
speedfilters = []
glidefilters = []
turnfilters = []
fadefilters = []
finalfilters = []

or_operator = ' | '
and_operator = ' & '

if args.full:
    print(csv)
    sys.exit(0)

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.mfgr:
    for i in range(len(args.mfgr)):
        mfgrfilters.append('(csv.Manufacturer == ' + "'" + args.mfgr[i] + "'" + ')')

if len(mfgrfilters) > 1:
    mfgrfinal = or_operator.join(mfgrfilters)
elif len(mfgrfilters) == 1:
    mfgrfinal = str(mfgrfilters)
else:
    mfgrfinal = None

if args.name:
    for i in range(len(args.name)):
        namefilters.append('(csv.Name == ' + "'" + args.name[i] + "'" + ')')

if len(namefilters) > 1:
    namefinal = or_operator.join(namefilters)
elif len(namefilters) == 1:
    namefinal = str(namefilters)
else:
    namefinal = None

if args.type:
    for i in range(len(args.type)):
        typefilters.append('(csv.Type == ' + "'" + args.type[i] + "'" + ')')

if len(typefilters) > 1:
    typefinal = or_operator.join(typefilters)
elif len(typefilters) == 1:
    typefinal = str(typefilters)
else:
    typefinal = None

if args.speed:
    for i in range(len(args.speed)):
        speedfilters.append('(csv.Speed == ' + args.speed[i] + ')')

if len(speedfilters) > 1:
    speedfinal = or_operator.join(speedfilters)
elif len(speedfilters) == 1:
    speedfinal = str(speedfilters)
else:
    speedfinal = None

if args.glide:
    for i in range(len(args.glide)):
        glidefilters.append('(csv.Glide == ' + args.glide[i] + ')')

if len(glidefilters) > 1:
    glidefinal = or_operator.join(glidefilters)
elif len(glidefilters) == 1:
    glidefinal = str(glidefilters)
else:
    glidefinal = None

if args.turn:
    for i in range(len(args.turn)):
        turnfilters.append('(csv.Turn == ' + args.turn[i] + ')')

if len(turnfilters) > 1:
    turnfinal = or_operator.join(turnfilters)
elif len(turnfilters) == 1:
    turnfinal = str(turnfilters)
else:
    turnfinal = None

if args.fade:
    for i in range(len(args.fade)):
        fadefilters.append('(csv.Fade == ' + args.fade[i] + ')')

if len(fadefilters) > 1:
    fadefinal = or_operator.join(fadefilters)
elif len(fadefilters) == 1:
    fadefinal = str(fadefilters)
else:
    fadefinal = None

if mfgrfinal:
    finalfilters.append(mfgrfinal)

if namefinal:
    finalfilters.append(namefinal)

if typefinal:
    finalfilters.append(typefinal)

if speedfinal:
    finalfilters.append(speedfinal)

if glidefinal:
    finalfilters.append(glidefinal)

if turnfinal:
    finalfilters.append(turnfinal)

if fadefinal:
    finalfilters.append(fadefinal)


finalargs = and_operator.join(finalfilters)
finalargs = re.sub(r'\[', r'', finalargs)
finalargs = re.sub(r'\]', r'', finalargs)
#finalargs = re.sub(r'^', r'[', finalargs)
#finalargs = re.sub(r'$', r']', finalargs)
finalargs = re.sub(r'"', r'', finalargs)

newcsv = 'print(csv[' + finalargs + '])'

print(finalargs)
print(newcsv)

exec(newcsv)
