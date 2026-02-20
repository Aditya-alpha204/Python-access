import urllib.request,urllib.parse,urllib.error
import json
import ssl

#SSL Setup (Always keep this for assignments)
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

surl="http://py4e-data.dr-chuck.net/opengeo?"

address=input('Enter location:')
if len(address)<1:
    print("Empty")
else:
    params=dict()
    params['q']=address
    url=surl+urllib.parse.urlencode(params)
    print("Reyrieving:",url)    
    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    print("Retrieved",len(data),"charactera")

    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'features' not in js or len(js['features'])==0:
            print("====Failure To Retrieve===")
            print(data)
    else:
            plus_code=js['features'][0]['properties']['plus_code']
            print('Plus code',plus_code)  

