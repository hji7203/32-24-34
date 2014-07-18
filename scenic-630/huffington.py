#-*-coding:utf-8-*-

from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs

os.mkdir("0707")
data = urlopen('http://www.huffingtonpost.kr/the-news/2014/07/07')
soup = BeautifulSoup(data)
for i in soup.findAll('h3'):
	print i.text
	title = i.text
	title = title.replace("?","")
	title = title.replace(":","")
	title = title.replace("'","")
	title = title.replace("!","")

	url = i.a.get('href')

	file = codecs.open("0707" + "/" +title + ".txt", "w", "utf-8")
	data_c = urlopen(url)
	soup_c = BeautifulSoup(data_c)
	
	for s in soup_c.findAll('p'):
		# s_text = s.text
		# print s_text
	# file = codecs.open(heading, "w", "utf-8")
		file.write(s.text)
	file.close()

			