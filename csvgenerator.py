import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

url = 'https://infinitediscs.com/category/'
mfgrs = ['ABC', 'Above-Ground-Level', 'AquaFlight', 'Arsenal-Discs', 'Axiom', 'Crosslap', 'Daredevil', 'DGA', 'Dino-Discs', 'Disc-Golf-UK', 'Discmania', 'Discraft', 'Disctroyer', 'Dynamic-Discs', 'Element-Discs', 'Fourth-Circle-Discs', 'Full-Turn', 'Galaxy-Disc-Golf', 'Gateway', 'Guru-Disc-Golf', 'Hyzer-Bomb', 'Infinite-Discs', 'Innova', 'Kastaplast', 'Kaufinator-Discs', 'Latitude-64', 'Launch-Disc-Golf', 'Legacy', 'Lightning-Discs', 'Millennium', 'Mint-Discs', 'MVP', 'Nite-Ize', 'Ozone-Discs', 'Plastic-Addicts', 'Prodigy', 'Prodiscus', 'Reptilian-Disc-Golf', 'RPM-Discs', 'Salient', 'Skyquest', 'Storm-Disc-Golf', 'Streamline', 'Thought-Space-Athletics', 'TOBU', 'Viking-Discs', 'Westside', 'XCom', 'Yikun']

df = pd.DataFrame(columns=['Name', 'Manufacturer', 'Speed', 'Glide', 'Turn', 'Fade'])

for i in mfgrs:
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
        each = f'{i},{each}'
        each = list(each.split(','))
        print(each)
        df = df.append(pd.DataFrame([each], columns=['Name', 'Manufacturer', 'Speed', 'Glide', 'Turn', 'Fade']), ignore_index=True)

df.to_csv('discs.csv', index=False)
