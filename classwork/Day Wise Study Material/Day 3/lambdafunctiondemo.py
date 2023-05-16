lst=[12,13,14,16,2,3,4,15]
lst2=[]
for v in lst:
    if v%4==0 and v>4:
        lst2.append(v)

print(lst2)

#list compression operator
lst3=[v for v in lst if v%4==0 and v>5]
print(lst3)


lst4=list(filter(lambda x:x%4==0 and x>5,lst))
print(lst4)

lst=[12,13,14,16,2,3,4,15]

lst1=[]
for v in lst:
    lst1.append(v*v)

print(lst1)
lst2=[v*v for v in lst]
print(lst1)

lst3=list(map(lambda x:x*x ,lst))


from functools import reduce

ans=reduce(lambda x,y:x+y,lst)
print("answer: ",ans)

ans=reduce(lambda x,y:x if x<y else y,lst)

lst3=["python","perl","os","c++","java"]

ans=reduce(lambda x,y:x if len(x)<len(y) else y ,lst3)
print(ans)

ans=reduce(lambda x,y:x+y[0:3],lst3,"")
print(ans)








