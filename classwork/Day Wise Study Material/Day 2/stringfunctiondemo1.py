s="this is cat, cat is cute, where is your cat"
pos=s.find("cat")
print(pos)
pos=s.find("cat",pos+1)
print(pos)
pos=s.find("cat",pos+1)
print(pos)
pos=s.find("cat",pos+1)
print(pos)

#write program to find all occurances of the given string
pos=s.find("cat")
while pos!=-1:
    print("position: ",pos)
    pos=s.find("cat",pos+1)
print("occurances of cat",s.count("cat"))
#s.index("dog")





    
