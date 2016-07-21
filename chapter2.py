# this is for pythonchallenge chapter 2

import string

def translate2(text):
    i=0
    while i<num:        
        if text[i] in letter:
            a=text[i]
            b=letter.index(a)
            c=(b+2)%26           
            text[i]=letter[c]
        i+=1
    return ''.join(text)

            
text=raw_input('paste the letter: ')
num=len(text)
text=list(text)
letter=string.ascii_lowercase

print translate2(text)
