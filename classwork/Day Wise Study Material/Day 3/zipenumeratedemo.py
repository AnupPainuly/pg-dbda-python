lst=[1,2,3]
lst1=["pune","mumbai","nashik","nagpur"]

#it will help us to navigate through multiple list parallely
for v,p in zip(lst,lst1):  #[(1,"pune"),(2,"mumbai)
    print(v,"--->",p)

lst=[12,1,3,14]

#search value in the list
s=3
cnt=0
for v in lst:
    if v==s:
        print(v,cnt)
        break
    cnt=cnt+1

#enumerate numbers the list, numbering starts with 0
for idx,v in enumerate(lst): #[(0,12),(1,1),(2,3)
    if v==s:
        print(v,idx)
        break
#enumerate numbers the list,it will start with 1
for idx,v in enumerate(lst,1):
    print(idx,".",v)

#it will pass data in the reverse order in the for loop
#it helps to print data in reverse order without changing the original list
for v in reversed(lst):
    print(v)
print(lst)

#sorted function will pass the data in the for loop in ascending order
#it display data in sorted order without changing original list
#sorted(lst,reverse=True) it will sort the data in descending order
for v in sorted(lst):
    print(v)

print(lst)
    








                          
        
