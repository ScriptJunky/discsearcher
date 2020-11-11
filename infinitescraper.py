import requests
from bs4 import BeautifulSoup as soup

url = 'https://infinitediscs.com/category/'
mfgrs = ['ABC', 'Above-Ground-Level', 'AquaFlight', 'Arsenal-Discs', 'Axiom', 'Crosslap', 'Daredevil', 'DGA', 'Dino-Discs', 'Disc-Golf-UK', 'Discmania', 'Discraft', 'Disctroyer', 'Dynamic-Discs', 'Element-Discs', 'Fourth-Circle-Discs', 'Full-Turn', 'Galaxy-Disc-Golf', 'Gateway', 'Guru-Disc-Golf', 'Hyzer-Bomb', 'Infinite-Discs', 'Innova', 'Kastaplast', 'Kaufinator-Discs', 'Latitude-64', 'Launch-Disc-Golf', 'Legacy', 'Lightning-Discs', 'Millennium', 'Mint-Discs', 'MVP', 'Nite-Ize', 'Ozone-Discs', 'Plastic-Addicts', 'Prodigy', 'Prodiscus', 'Reptilian-Disc-Golf', 'RPM-Discs', 'Salient', 'Skyquest', 'Storm-Disc-Golf', 'Streamline', 'Thought-Space-Athletics', 'TOBU', 'Viking-Discs', 'Westside', 'XCom', 'Yikun']

everything = []

for i in mfgrs:
    everything.append('starting ' + i + ('\n'))
    idurl = requests.get(url + i).text
    soupf = soup(idurl, 'html')
    everything.append(soupf.find_all('h4'))
    everything.append('closing ' + i + ('\n'))

for i in everything:
    print(i)
