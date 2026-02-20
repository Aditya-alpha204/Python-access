import re
import math
fil=input("Enter file:")
handle=open(fil)
su=0
y=list()
for line in handle:
    y=re.findall('([0-9]+)',line)
    for num in y:
        su=su+int(num)
print(su)
 
