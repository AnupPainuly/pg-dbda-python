#[ 1+x+x^2/2!+x^3/3!+....]
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

x=int(input("enetr number"))
term=int(input("enetr number of terms"))
s=1
f=1
print(f"1",end="")
for i in range(1,term):
    #f=factorial(i)
    f=f*i  #1*2*3*4
    s=s+((x**i)/f)
    print(f"+{x}^{i}/{i}!",end="")
print("=answer: ",s)

#for loop in reverse order
for i in range(5,1,-1):
    print(i)
    

