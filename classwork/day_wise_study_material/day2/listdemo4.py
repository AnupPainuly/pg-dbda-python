lst=[12,1,3,14,15,34,7,12,3,14,12]
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print(lst.count(12))

lst=[1,2,3]
lst1=lst
lst.append(34)
print(lst,lst1)
lst2=lst.copy()
lst.append(100)
print(lst,lst1)
print(lst2)


