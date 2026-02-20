name = input("Enter file:")
op=open(name)
lst=list()
dic=dict()
k=0
for line in op:
    if line.startswith("From "):
        lst=line.split(" ")
        email=lst[1]
        dic[email]=dic.get(email,0)+1
bcount=None
bemail=None
for email in dic:
    count=dic[email]
    if bcount is None or count>bcount:
        bemail=email
        bcount=count
print(bemail,bcount)        
           