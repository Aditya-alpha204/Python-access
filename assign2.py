# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#setup SSL
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url,context=ctx).read()
count=int(input("Enter times"))
pos=int(input("Enter postion"))
print("Retrieving:",url)
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')

for i in range (count):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    url=(tags[pos-1].get('href', None))
    print("Retrieving:",url)
