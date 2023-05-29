#accept a number user check whether it is prime or not
num=int(input("enetr number"))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag:  #flag==True:
    print("number is not prime")
else:
    print("number is prime")

print("*"*60)

num=int(input("enetr number"))
for i in range(2,num):
    if num%i==0:
        print("number is not prime")
        break
else:
    print("number is prime")






    
