import requests
from bs4 import BeautifulSoup
import html5lib
url = 'https://yossiabramov.com/'
r = requests.get(url)
hc = r.content
#print(hc)

# Parse the html
soup = BeautifulSoup(hc,'html.parser')


anchor = soup.find_all('a')
#print(anchor)

all_links = set()

for li in anchor:
    if(li != '#'):
        li = "https://yossiabramov.com" + li.get('href')
        all_links.add(li)
        print(li)
        




