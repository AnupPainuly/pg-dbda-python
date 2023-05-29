#function returns a tuple of size 2
def f1(x,y):
    x=x+10
    y=y+20
    return x,y

#default parameter
def f2(a,b=56,c=34):
    print(a,b)
    a=a+45
    print(a,b)

#addition accepts 1 manditory parameter, 2 optional parameter
# and in t variable number of parameter, t is of type tuple
def addition(a,b=10,c=3,*t):
    s=a+b+c
    for val in t:
        s=s+val
    return s

print(addition(10))
print(addition(2,5))
print(addition(2,5,4,6,3,12,3,4,5,6))
        
    

f2(2,4)
a=20
b=30
p,q=f1(a,b)
