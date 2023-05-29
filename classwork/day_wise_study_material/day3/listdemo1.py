lst=[abcd,13,33,"xx",[10,20,30]]
print(lst[3])
print(lst[4][1])
lst[1]="abcd"
print(lst)
print(lst[2:])

#add data in the list
lst.append(45)
lst.insert(2,100)
print(lst)
lst2=["aaa","bbb","ccc"]
lst.extend(lst2)

print(lst,lst2)
#delete the data from the list
print(lst)
lst.pop()
print(lst)

# to delete the data from given position
lst.pop(3)
print(lst)

#remove by value
lst.remove(23)
lst.remove(33)













      


