import re
s="Something is there somewhere"
#findall searches all occurrences of the patteren any where in the
#string and return a list of strings
lst=re.findall("s.*?e",s,re.I)
if lst!=None:
    print(lst)
    
else:
    print("not found")



s="Something is there somewhere"
#finditer searches all occurrences of the patteren any where in the
#string and return a list of match object
lst=re.finditer("s.*?e",s,re.I)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
    
else:
    print("not found")
