import requests
import bs4
import html5lib

url = "https://yossiabramov.com/"
req = requests.get(url)
data = req.content
soup = bs4.BeautifulSoup(data,'html.parser')

### for title ###

title = soup.title

print(soup.find('title').get_text())



### for full html Content ###

print(soup.prettify())




