import requests
import bs4
import html5lib

url ="https://christianheilmann.com/"

req = requests.get(url)
data = req.content

soup = bs4.BeautifulSoup(data,"html.parser")

content = soup.prettify()

T = soup.title.text
print(T)

#print(content)

# article = soup.find('article')
for article in soup.find_all('article'):

    headline = article.h2.a.text
    print("ARTICLE'S HEADLINE IS : " + headline)
    
    summary = article.find('div').p.text
    print("ARTICLE'S SUMMARY IS : "+summary)

    publish = article.small.text
    print("ARTICLE'S PUBLISH DATE IS : "+publish)

   

