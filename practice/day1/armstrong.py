#Armstring number
num=int(input("enter the num: "))

#power
n=len(str(num))
res=0
for digit in str(num):
    res=res+int(digit)**n
if res == num:
    print("Armstrong Number")
else:
    print("Not An Armstrong Number")
