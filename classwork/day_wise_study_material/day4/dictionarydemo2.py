d1={"python":333,".net":444,"c++":555}
for k in d1.keys():
    print(k,"-->",d1[k])

for k,v in d1.items():
    if v>400:
        print(k,"-->",v)

lst=["A","B","C"]
d1=dict.fromkeys(lst)
print(d1)
d2=dict.fromkeys(lst,100)
print(d2)

d1={"a":10,"b":20}
d2={"b":40,"c":70}
#add all the keys from d2 to d1
d1.update(d2)
print(d1)  #{"a":10,"b":40,"c":70}

d1={"a":10,"b":20,"c":70,"d":56,"x":89}
#delete the last key-value pair
k,v=d1.popitem()
print(k,v)  #"x" 89
print(d1) #{"a":10,"b":20,"c":70,"d":56}

#to delete the key -value pair if key is given
k="b"
#it will delete key-value pair if key exists otherwise return -1
v=d1.pop(k,-1)
print(k,"-->",v)
print(d1)  ##{"a":10,"c":70,"d":56}







