import urllib.request ,urllib.parse ,urllib.error
import json
import ssl

#SSL Setup (Always keep this for assignments)
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter url:")
data=urllib.request.urlopen(url,context=ctx).read().decode()
info=json.loads(data)

dic=dict()
su=0
for item in info['comments']:
    su=su+int(item['count'])
print(su)    
