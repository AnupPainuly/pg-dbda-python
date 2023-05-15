a=9
b=13
print(bin(a))
print(bin(b))

#compression
d=a<<4
print(bin(d))
x=d|b
print(bin(x),x)

print("and mask",int(0b1111))
#decompress
b=x&(int(0b1111))
print("b",b)
a=x>>4
print("a",a)
        
