# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
tsum=0
count=0
for tag in tags:
   num=int(tag.contents[0])
   tsum+=num
   count+=1
print('sum',tsum)
print('count',count)