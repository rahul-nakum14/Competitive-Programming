import requests
from bs4 import BeautifulSoup

request = requests.get('https://coreyms.com')

soup = BeautifulSoup(request.text,'html.parser')

tmp = soup.find('article')
# print(tmp.h2.a.text) #print headline


# summy = tmp.find('div',class_='entry-content')
# print(summy.p.text)



vdo = tmp.find('iframe',class_='youtube-player')['src']
print(vdo)

id = vdo.split('/')[4]
id = id.split('?')[0]
print(id)
