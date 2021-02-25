from urllib.request import *
from bs4 import BeautifulSoup
import re
import operator
from collections import Counter
import string

dict = {}
list = []
for i in range(65,91):
    for j in range(65,91):

        file = urlopen("https://en.wikipedia.org/wiki/"+chr(i)+chr(j))
        str = file.read()
        objhtml = BeautifulSoup(str,"html.parser")
        for element in objhtml(["script","style"]):
            element.extract()
        str_text = objhtml.get_text()
        p = '[a-zA-Z]+'
        regex = re.compile(p,re.IGNORECASE)
        for m in regex.finditer(str_text):
            list.append(m.group())
        for r in list:
            if r in dict :
                dict[r]+=1
            else:
                dict[r]=1
        print("Done "+chr(i)+chr(j))
        list.clear()
d = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
check = 0
while(check<15):
    print(d[check])
    #print(d.get(check).key+" "+d.get(check).value)
    check += 1



