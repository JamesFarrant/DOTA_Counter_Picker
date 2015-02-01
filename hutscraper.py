from urllib.request import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://www.dotahut.com/heroes/pudge')
soup = BeautifulSoup(f)
heroList = soup.findAll('div', attrs={'class': 'name'})
for i in heroList:
    print(i)
