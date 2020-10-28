import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

sys.setrecursionlimit(5000)

url = urlopen('http://www.inboundsdiscgolf.com/content/?page_id=431')
bs = BeautifulSoup(url, 'html.parser')
discs = bs.find_all('td', {'class': 'lp'})

for x in range(len(discs)):
    plastic = str(discs[x].findChildren()).replace('|', '\t')
    notail = plastic[:-4]
    nohead = notail[43:]
    tidied = str(nohead).replace("&amp;", "&")
    print(tidied)
