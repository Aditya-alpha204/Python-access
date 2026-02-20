import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
dic=dict()
for line in fhand:
    print(line.decode().strip())
    k=line.decode().split()
    for word in k:
        dic[word]=dic.get(word,0)+1
print(dic)