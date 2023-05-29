d1={"Python":234,"java":456,"c++":200}
#print all keys
print(d1.keys())
#print all values
print(d1.values())
#since key is not there it will add new key value pair

d1[".net"]=345
print(d1)
#since key exists it will overwrite the value
d1["python"]=345

#if key is known then to retrieve the value if key exists
#otherwise throws exception
print(d1["python"])


v=d1.get("python")
if v!=None:
    print("key found",v)
else:
    print("key not found")
    
v=d1.get("python1",-1)
if v!=-1:
    print("key found",v)
else:
    print("key not found")

v=d1.setdefault("python1",100)
print(d1)

    


