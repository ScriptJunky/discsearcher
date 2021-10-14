#!/usr/bin/env python
import argparse
import numpy as np
import os
import pandas as pd
import re
import requests
import socket
from bs4 import BeautifulSoup as soup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

parser = argparse.ArgumentParser()
parser.add_argument('--un', help=argparse.SUPPRESS)
parser.add_argument('--pw', help=argparse.SUPPRESS)
args = parser.parse_args()

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
vnum = 2020.364
version = f'''
discsearcher v{vnum}
\u00A9 2020 - Throw The Roller, LLC.
{contact}
'''

# Elements needed for URL generation
url = 'https://infinitediscs.com'
referral = '?tag=3c8c6529'

# Some known disc name translations
discdictionary = {
    '#1 Driver': 'No1-Driver',
    '#1 Flyer': 'No1-Flyer',
    '#1 Helix': 'No1-Helix',
    '#1 Hookshot': 'No1-Hookshot',
    '#1 Hyzer': 'No1-Hyzer',
    '#1 Roller': 'No1-Roller',
    '#1 Slice': 'No1-Slice',
    '#2 Driver': 'No2-Driver',
    '#2 Flyer': 'No2-Flyer',
    '#2 Helix': 'No2-Helix',
    '#2 Hookshot': 'No2-Hookshot',
    '#2 Hyzer': 'No2-Hyzer',
    '#2 Putter': 'No2-Putter',
    '#2 Roller': 'No2-Roller',
    '#2 Slice': 'No2-Slice',
    '#2 Upshot': 'No2-Upshot',
    '#3 Driver': 'No3-Driver',
    '#3 Flyer': 'No3-Flyer',
    '#3 Hookshot': 'No3-Hookshot',
    '#3 Hyzer': 'No3-Hyzer',
    '#3 Slice': 'No3-Slice',
    '#4 Driver': 'No4-Driver',
    '10 Meter Crossfire': '10-Meter-Crossfire',
    'Aurora MS': 'Aurora-MS',
    'Avenger SS': 'Avenger-SS',
    'Aviar Classic': 'Aviar-Classic',
    'Aviar Driver': 'Aviar-Driver',
    'Aviar Yeti': 'Aviar-Yeti',
    'Aviar-X (JK)': 'Aviar-X-(JK)',
    'Ballista Pro': 'Ballista-Pro',
    'Banger GT': 'Banger-GT',
    'Big Foot': 'Big-Foot',
    'Blowfly I': 'Blowfly-I',
    'Blowfly II': 'Blowfly-II',
    'Blunt Gumbputt': 'Blunt-Gumbputt',
    'Buzzz GT': 'Buzzz-GT',
    'Buzzz OS': 'Buzzz-OS',
    'Buzzz SS': 'Buzzz-SS',
    'CD': 'CD-Craze',
    'Catapult ': 'Catapult',
    'Catapult': 'Catapult',
    'Challenger OS': 'Challenger-OS',
    'Challenger SS': 'Challenger-SS',
    'Chief OS': 'Chief-OS',
    'Classic Roc': 'Classic-Roc',
    'Claws': 'Talon-(Claws)',
    'Code X': 'Code-X',
    'Crank SS': 'Crank-SS',
    'D Model OS': 'D-Model-OS',
    'D Model S': 'D-Model-S',
    'D Model US': 'D-Model-US',
    'D Model US+': 'D-Model-US-Plus',
    'D Model US++': 'D-Model-US-Plus-Plus',
    'D1 Max': 'D1-Max',
    'D2 ': 'D2-',
    'D2 Max': 'D2-Max',
    'D3 Max': 'D3-Max',
    'D4 Max': 'D4-Max',
    'DD': 'DD-Hysteria',
    'DD2': 'DD2-Frenzy',
    'DD3 ': 'DD3',
    'Devil Hawk': 'Devil-Hawk',
    'EMac Judge ': 'EMac-Judge-',
    'EMac Truth': 'EMac-Truth',
    'Enigma': 'Evolution-Enigma',
    'F Model OS': 'F-Model-OS',
    'F Model OS+': 'F-Model-OS-Plus',
    'F Model S': 'F-Model-S',
    'F Model US': 'F-Model-US',
    'FL': 'Firebird-FL',
    'Flathead Cyclone': 'Flathead-Cyclone',
    'Flow Motion': 'Flow-Motion',
    'Gray Jay': 'Gray-Jay',
    'Great Horned Owl': 'Great-Horned-Owl',
    'Gremlin GM': 'Gremlin-GM',
    'Grym X': 'Grym-X',
    'H1 V2': 'H1-V2',
    'H2 V2': 'H2-V2',
    'H3 V2': 'H3-V2',
    'H4 V2': 'H4-V2',
    'Hammer (Chui)': 'Hammer-(Chui)',
    'I One': 'I-One',
    'Jet Stream': 'Jet-Stream',
    'Judge ': 'Judge',
    'KC Aviar': 'Aviar-KC-Pro',
    'Kahu OS': 'Kahu-OS',
    'Kahu XG': 'Kahu-XG',
    'Kaufinator Aftermath': 'Kaufinator-Aftermath',
    'Kaufinator Bandit': 'Kaufinator-Bandit',
    'Kaufinator Cannon': 'Kaufinator-Cannon',
    'Kaufinator Gauge': 'Kaufinator-Gauge',
    'Kaufinator Ghost': 'Kaufinator-Ghost',
    'Kaufinator Nemesis': 'Kaufinator-Nemesis',
    'Kaufinator Outlaw': 'Kaufinator-Outlaw',
    'Kaufinator Phenom': 'Kaufinator-Phenom',
    'Kaufinator Pursuit': 'Kaufinator-Pursuit',
    'Kaufinator Rampage': 'Kaufinator-Rampage',
    'Kaufinator Rival': 'Kaufinator-Rival',
    'Kaxe Z': 'Kaxe-Z',
    'King Cobra': 'King-Cobra',
    'Kon Tiki': 'Kon-Tiki',
    'LED Driver': 'LED-Driver',
    'LED Midrange': 'LED-Midrange',
    'LED Putter': 'LED-Putter',
    'Luan': 'Lu',
    'Lucky 13': 'Lucky-13',
    'M Model OS': 'M-Model-OS',
    'M Model S': 'M-Model-S',
    'M Model US': 'M-Model-US',
    'MD2': 'MD2-Fiend',
    'Mad Cat': 'Mad-Cat',
    'Mad Mission': 'Mad-Mission',
    'Meteor Hammer': 'Meteor-Hammer',
    'Night Trooper': 'Night-Trooper',
    'Nordic Warrior': 'Nordic-Warrior',
    'Nuke OS': 'Nuke-OS',
    'Nuke SS': 'Nuke-SS',
    'Odyssey Distance Driver': 'Odyssey-Distance-Driver',
    'Omega AP Big Bead': 'Omega-AP-Big-Bead',
    'Omega AP': 'Omega-AP',
    'Omega Big Bead': 'Omega-Big-Bead',
    'Omega Driver': 'Omega-Driver',
    'Omega SuperSoft': 'Omega-SuperSoft',
    'Orion LF': 'Orion-LF',
    'Orion LS': 'Orion-LS',
    'P Model S': 'P-Model-S',
    'P Model US': 'P-Model-US',
    'PD': 'PD-Freak',
    'PD2': 'PD2-Chaos',
    'Peace Frog': 'Peace-Frog',
    'Penny Putter': 'Penny-Putter',
    'Phantom Warrior': 'Phantom-Warrior',
    'Polar Bear': 'Polar-Bear',
    'Polaris LF': 'Polaris-LF',
    'Polaris LS': 'Polaris-LS',
    'PowerDrive Gumbputt': 'PowerDrive-Gumbputt',
    'Prototype 3': 'Prototype-3',
    'Raging Inferno': 'Raging-Inferno',
    'Rancho Roc': 'Rancho-Roc',
    'Razor Claw Tactic': 'Razor-Claw-Tactic',
    'Ringer GT': 'Ringer-GT',
    'River Pro': 'River-Pro',
    'Roc +': 'Roc-',
    'Rubber Putter': 'Rubber-Putter',
    'Saint Pro': 'Saint-Pro',
    'Sentinel MF': 'Sentinel-MF',
    'Shooting Star': 'Shooting-Star',
    'Short Slacker': 'Short-Slacker',
    'Silent Cruiser': 'Silent-Cruiser',
    'Soft Magnet': 'Soft-Magnet',
    'Speed Demon': 'Speed-Demon',
    'Steady BL': 'Steady-BL',
    'Super Stingray': 'Super-Stingray',
    'Surge SS': 'Surge-SS',
    'Swan 1 Reborn': 'Swan-1-Reborn',
    'Swift Fox': 'Swift-Fox',
    'TD': 'TD-Rush',
    'TD2 Fever': 'TD2-Fever',
    'TeeBird +': 'TeeBird-',
    'The Adder': 'The-Adder',
    'The Adder': 'The-Adder',
    'The Baron': 'The-Baron',
    'The Count': 'The-Count',
    'The Duchess': 'The-Duchess',
    'The Duke': 'The-Duke',
    'Thunder God Thor': 'Thunder-God-Thor',
    'Training Wizard': 'Training-Wizard',
    'Turbo Putt II': 'Turbo-Putt-II',
    'Turbo Putt': 'Turbo-Putt',
    'Twin Swords': 'Twin-Swords',
    'Tyrannosaurus Rex': 'Tyrannosaurus-Rex',
    'Wall Cloud': 'Wall-Cloud',
    'War Horse': 'War-Horse',
    'XD +': 'XD-',
    'Zion Driver': 'Zion-Driver',
}

mfgrs = []
mfgrnames = []

mainpage = session.get(url).text
soupf = soup(mainpage, 'lxml')

for i in soupf.find_all('a', attrs={'href': re.compile("/category/")}):
    mfgrs.append(i)

for m in mfgrs:
    m = str(m).split('"')
    mfgrnames.append(m[1])

mfgrnames = np.unique(mfgrnames)

df = pd.DataFrame(columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth'])
#df = pd.DataFrame(columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth', 'Plastics'])

for i in mfgrnames:
    idurl = session.get(url + i).text
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
#        plastics = []
        each = f'{i.replace("/category/", "")},{each}'
        each = list(each.split(','))
        each[2] = float(each[2].replace("'", ""))
        each[3] = float(each[3].replace("'", ""))
        each[4] = float(each[4].replace("'", ""))
        each[5] = float(each[5].replace("'", ""))
        name = each[1]
        if name in discdictionary:
            name = discdictionary.get(name)
        name = re.sub(r' ', '-', name)
        name = re.sub(r"'", '', name)
        name = re.sub(r'-$', '', name)
        name = re.sub(r'\+$', '-', name)
        name = re.sub(r'--$', '-', name)
        dimurl = url + '/' + each[0] + '-' + name
        discpage = session.get(dimurl).text
        soupf = soup(discpage, 'lxml')
        try:
            diameter = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblDiameter'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        except:
            diameter = 0
        each.append(diameter)
        try:
            height = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblHeight'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        except:
            height = 0
        each.append(height)
        try:
            rimdepth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimDepth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        except:
            rimdepth = 0
        each.append(rimdepth)
        try:
            rimwidth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimWidth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        except:
            rimwidth = 0
        each.append(rimwidth)
#        for x in soupf.find_all('a', {'class': 'btn btn-info btn-xs'}):
#            plastics.append(x.get_text().rstrip())
#        each.append(plastics)
        print(each)
        df = df.append(pd.DataFrame([each], columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth']), ignore_index=True)
#        df = df.append(pd.DataFrame([each], columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth', 'Plastics']), ignore_index=True)

df['Purchase Url'] = url + '/' + df['Manufacturer'] + '-' + df['Name'].replace(discdictionary) + referral

df.drop_duplicates(inplace=True, ignore_index=True)

df.to_csv('discs.csv', index=False)

# Let's go ahead and ship it off to bitbucket
uploadfile = {'files': open('discs.csv', 'rb')}
credentials = {
    'user': args.un,
    'password': args.pw
}

url = 'https://api.bitbucket.org/2.0/repositories/biscuits/discsearcher/downloads'
r = requests.post(url, auth=(args.un, args.pw), files=uploadfile)
