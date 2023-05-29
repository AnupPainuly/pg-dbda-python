import re
s="Something is there somewhere"

#substitute will replace all occurence by given string,
#by default count is 0, but if you specify count then it will replace count
#number of occurrence 
s1=re.sub("s.*?e","any",s,flags=re.I)
#s1=re.sub("s.*?e","any",s,flags=re.I,count=2)
print(s1)

#it will create a regexp object
myreg=re.compile("s.*?e",re.I)
s1=myreg.sub("any",s)
print(s1)

m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
