import requests
import bs4
import html5lib
import sqlite3

conn = sqlite3.connect('mysite.db')
c = conn.cursor()

#c.execute('''CREATE TABLE data(headline TEXT , summary TEXT , Publish_date TEXT)''')


url ="https://christianheilmann.com/"

req = requests.get(url)
data = req.content

soup = bs4.BeautifulSoup(data,"html.parser")

content = soup.prettify()

T = soup.title.text
# print(T)

# #print(content)

# # article = soup.find('article')
for article in soup.find_all('article'):

    headline = article.h2.a.text
#     print(headline)
    
    summary = article.find('div').p.text
#     print(summary)

    publish = article.small.text
#     print(publish)

    c.execute('''INSERT INTO data VALUES(?,?,?)''',(headline,summary,publish))

conn.commit()
print('COMPLETE')

# c.execute('''SELECT * FROM data''')
# results = c.fetchall()
# print(results)

conn.close()