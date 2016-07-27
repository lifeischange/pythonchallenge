content=web.read()
#关闭
web.close()

#正则匹配需要的字符串
regex=re.compile(r'<img src="\w+\.png"')
pct=re.search(regex,content).group()
#下载匹配好的文件
urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png','1.png')

#采用图像解析打开文件
im=Image.open('1.png')
#打印下载文件的各项参数
area=(0,43,608,52)
obj=im.crop(area)

body=obj.getdata()

tbody=obj.convert('L')

next=tbody.getdata()

mtr=np.array(next)

mtr=mtr[::7]

ok=''.join([chr(i) for i in mtr])

nextlink=re.search(r'.+?(?=smart)',ok).group()
answer=re.findall(r'\d+',nextlink)
for i in answer:
    print chr(int(i)),
