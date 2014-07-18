
# import os
# os.rmdir("Daye")
# print os.path.abspath('.')
from urlib import urlopen
from bs4 import BeautifulSoup

data = urlopen('')

soup = BeautifulSoup(data)
for font_name in soup.findAll('')
	print font_name['']