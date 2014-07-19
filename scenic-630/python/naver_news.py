#-*-coding:utf-8-*-

from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs
import urllib2


# os.mkdir("naver_news")
data = urlopen('http://openapi.naver.com/search?key=a4cfe50c6eea2848a097c5b77f0bf32f%20&query=%EB%94%B8%EA%B8%B0&target=news&start=1&display=20')
soup = BeautifulSoup(data)
j=0
for i in soup.findAll('item'):
	j += 1
 	file = open("naver_news" + "/" +"news" + str(j) + ".html", "w")
 	link = i.findAll('link')[0].text
 	print link
 	data_c = urlopen(link)
	soup_c = BeautifulSoup(data_c, from_encoding= 'utf-8')
	file.write(soup_c.encode('utf-8'))
	file.close()

			