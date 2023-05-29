s={12,1,31,100,2,1,1}
print(s)
#to convert string to set, to remove duplicate characters

s1=set("This is string")
print(s1)

#to convert list to set, to remove duplicate strings

s2=set(["python","Perl","python","os", "c++"])
print(s2)

print(s)
#add number to set
s.add(34)
#add string to set
s.add("xxx")
#add tuple to set
s.add((92,3,"vvv"))
print(s)
#s.add([1,2,3]) #error

#to add all values of iterable objects into another set
s.update(s2)
print(s)

#to delete random value from the set
v=s.pop()
print(v)
print(s)

#to delete the given value
s.remove("python")
print(s)

s.remove("python")










