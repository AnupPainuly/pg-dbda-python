
for i in range(10): #0,1,2,3,...9
    print(i,end=" ")
print()

for i in range(2,10): #2,3,...9
    print(i,end=" ")

print()
#           (start,end,step)
for i in range(0,20,2): #0,2,4,6...,18
     print(i,end=" ")

print()

num=int(input("enter number"))
f=1
for i in range(1,num+1):
    f=f*i
print(f)
