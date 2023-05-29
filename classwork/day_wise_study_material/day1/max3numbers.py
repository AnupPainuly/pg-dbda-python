#write a program to find maximum of 3 numbers
a=int(input("enter number1"))
b=int(input("enter number2"))
c=int(input("enter number3"))
if a>b and a>c:
    print("a is greater"+str(a))
    print("a is greater",a)
elif b>a and b>c:
    print("b is greater"+b)
else:
    print("c is greater"+c)
