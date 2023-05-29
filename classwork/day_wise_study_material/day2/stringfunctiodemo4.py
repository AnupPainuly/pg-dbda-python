s="this is strin#$ g123 , test"
for ch in s:
    #it checks whether given string contains all alphabets
    #if ch.isalpha():
    #if ch.isalnum():
    if ch.isdecimal():
        print(ch)

s="Hello"
t="Hello"
f=s
print(id(s),id(t),id(f))
s="test"
print(id(s),id(t),id(f))
print(s is t)
print(f is t)
x=input("enetr String")
print(x is t)
