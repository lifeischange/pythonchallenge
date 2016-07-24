import urllib2
import re

content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

text=content.read()

result=re.findall(r'(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])',text)
result=''.join(result)
print result
