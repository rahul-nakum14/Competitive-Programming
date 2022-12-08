import requests
from bs4 import BeautifulSoup

with open('simple.html') as htmlfile:
    soup = BeautifulSoup(htmlfile,'html.parser')
    # print(soup.div) return first div tag   print(soup.find('div'))  also first

    '''print footer'''
    # tmp = soup.find('div',class_="footer")
    # print(tmp.p.text)

    '''printing article'''
    tmp = soup.find('div',class_='article')
    # print(tmp.h2.a.text) #printing arcticle first headline
    # print(tmp.p.text)   #print summey of article 1


    '''printing all article at once'''

    for i in soup.find_all('div',class_='article'):
        print(i.h2.a.text)
        print(i.p.text)
