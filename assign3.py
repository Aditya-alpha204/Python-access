import urllib.request
import xml.etree.ElementTree as ET
import ssl

#SSL Setup (Always keep this for assignments)
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Make sure to copy the 'Actual data'
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)

#Retrieve (The "Delivery")
#'data' is just a long string of text right now
data = urllib.request.urlopen(url,context=ctx).read()
context = data.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

#Search for Tags
#We want to find every <count> tag.
#'.//count' means "find a tag named count anywhere in the tree"
counts = tree.findall('.//count')

print('counts:',len(counts))

tsum=0

for item in counts:
    tsum=tsum+int(item.txt)
print('Sum:', tsum)

