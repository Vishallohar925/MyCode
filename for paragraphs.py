import requests
import bs4
import html5lib

url = "https://yossiabramov.com/"
req = requests.get(url)
data = req.content
soup = bs4.BeautifulSoup(data,'html.parser')


###for all paragraphs###

for para in soup.find_all('p'):
   print(para.text)


