import zipfile,os,re

dirname=os.path.abspath(os.path.dirname(__file__))
files=os.path.join(dirname,'channel.zip')
start='90052'
while start:
    zips=zipfile.ZipFile(files)
    text=zips.getinfo('%s.txt'%start)
    print text.comment,
    text=zips.read('%s.txt'%start)
    zips.close()
    try:
        start=re.search(r'\d+',text).group()
    except AttributeError,e:
        print text
        break
        
