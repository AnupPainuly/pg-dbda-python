num=int(input("enetr number"))  #3456
s=0
while num >0:
    d=num%10     # 6  5  4  3
    num=num//10  #345  34 3  0
    s=s+d       #6 11  15   18

print("sum: ",s)
