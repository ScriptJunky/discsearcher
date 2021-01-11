import numpy as np
import os
import pandas as pd
import re
import requests
import socket
from bs4 import BeautifulSoup as soup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

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
    'CD': 'CD-Craze',
    'DD': 'DD-Hysteria',
    'DD2': 'DD2-Frenzy',
    'DD3 ': 'DD3',
    'Enigma': 'Evolution-Enigma',
    'PD': 'PD-Freak',
    'PD2': 'PD2-Chaos',
    'TD': 'TD-Rush',
    'MD2': 'MD2-Fiend',
    'FL': 'Firebird-FL',
    'KC Aviar': 'Aviar-KC-Pro',
    'TeeBird +': 'TeeBird-',
    'Roc +': 'Roc-',
    'XD +': 'XD-',
    'Luan': 'Lu',
    'Claws': 'Talon-(Claws)',
    'D Model US+': 'D-Model-US-Plus',
    'D Model US++': 'D-Model-US-Plus-Plus',
    'F Model OS+': 'F-Model-OS-Plus'
}

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

df = pd.DataFrame(columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth'])
#df = pd.DataFrame(columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth', 'Plastics'])

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
        discpage = requests.get(dimurl).text
        soupf = soup(discpage, 'lxml')
        diameter = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblDiameter'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        each.append(diameter)
        height = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblHeight'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        each.append(height)
        rimdepth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimDepth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        each.append(rimdepth)
        rimwidth = float(soupf.find('li', {'id': 'ContentPlaceHolder1_lblRimWidth'}).get_text().split(':')[1].lstrip().replace(' cm', ''))
        each.append(rimwidth)
#        for x in soupf.find_all('a', {'class': 'btn btn-info btn-xs'}):
#            plastics.append(x.get_text().rstrip())
#        each.append(plastics)
        print(each)
        df = df.append(pd.DataFrame([each], columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth']), ignore_index=True)
#        df = df.append(pd.DataFrame([each], columns=['Manufacturer', 'Name', 'Speed', 'Glide', 'Turn', 'Fade', 'Diameter', 'Height', 'RimDepth', 'RimWidth', 'Plastics']), ignore_index=True)

df['Purchase Url'] = url + '/' + df['Manufacturer'] + '-' + df['Name'].replace(discdictionary) + referral

df.to_csv('discs.csv', index=False)
