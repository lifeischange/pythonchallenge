import urllib
import urllib2
import re

i=0
nothing='12345'
while i<400:

    response=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
    text=response.read()
    response.close()
    print text
    try:
        num=int(nothing)
        no=re.search(r'\d+',text)
        nothing=no.group()
        print nothing
        
    except Exception:
        print text
        nothing=str(num/2)
    i+=1

