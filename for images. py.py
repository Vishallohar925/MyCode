import requests
from bs4 import BeautifulSoup
import html5lib
url = 'https://yossiabramov.com/'
r = requests.get(url)
hc = r.content
#print(hc)

# Parse the html
soup = BeautifulSoup(hc,'html.parser')


### for Images link ###

anchor = soup.find_all('img')
#print(anchor)

for i in anchor:
    print(i.get('src'))


