import urllib.request
import xml.etree.ElementTree as ET

url=input("Enter location:")
print("Retrieving:",url)
uh=urllib.request.urlopen(url)
l=uh.read()
print("Retrieved",len(l),"characters")


tree=ET.fromstring(l)
lst=tree.findall('.//count')
t=0
for item in lst:
    t=t+int(item.text)
print("count:",len(lst))
print("sum:",t)    

