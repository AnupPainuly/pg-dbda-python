import re

s="Something is there somewhere"
m=re.search("t.*?e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")


s="Something is there somewhere"
m=re.match("t.*?e",s,re.I)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
