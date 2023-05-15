s="abc:pqr:xyz:test,try"
print(s.upper())
print(s.lower())
lst=s.split(":")
print(lst)
s1="|".join(lst)
print(s1)
#it will replace all occurances
s2=s.replace(":","|")
print(s2)

s2=s.replace(":","|",1)
#it replace only 1 st occurance
print(s2)
