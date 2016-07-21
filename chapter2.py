# this is for pythonchallenge chapter 2.1

from string import maketrans
import string

def fix2(words):
    text=string.ascii_lowercase
    text2=text[2:]+'ab'
    temp=maketrans(text,text2)
    result=words.translate(temp)
    return result
words="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print fix2(words)






