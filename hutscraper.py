from urllib.request import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://www.dotahut.com/heroes/faceless_void')
soup = BeautifulSoup(f)
heroList = soup.findAll('div', attrs={'class': 'weak-block'})
# Check the first block of HTML for the counter-hero names
weak_hero = heroList[0].findAll('div', attrs={'class': 'name'})

for i in weak_hero:
    print(i.text)
