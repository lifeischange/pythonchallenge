import urllib2
import pickle

url=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
context=url.read()
url.close()

f=open('het.txt','wb')
f.write(context)
#pickle.dump(context,f,True)
f.close()

f=open('het.txt','rb')
text=pickle.load(f)
f.close()
for lines in text:
    a=''
    for line in lines:
        a+=line[0]*line[1]
    print a   
