#__author__ = 'DKjack'
#coding=utf--8

from urllib.request import urlopen
from bs4 import  BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
if html is None:
    print("URL is not found")
else:
    bsObj =BeautifulSoup(html.read())

print(bsObj.h1)
print(bsObj.nonExistTag.someTag)