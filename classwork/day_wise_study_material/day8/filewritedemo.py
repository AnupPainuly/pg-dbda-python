# -*- coding: utf-8 -*-
"""
Created on Sun May 21 09:37:14 2023

@author: anilk
"""
def writedatatofile(fh):
    ans="y"
    while ans=="y":
        pid=input("enetr product id")
        pname=input("enetr pname")
        qty=input("enter qty")
        price=input("enetr price")
        fh.write(f"{pid}:{pname}:{qty}:{price}\n")
        ans=input("Continue(y/n)?")
    
import os
if os.path.exists("newprod.txt"):
    with open("newprod.txt","a") as fh:
        writedatatofile(fh)
else:
    with open("newprod.txt","w") as fh:
        writedatatofile(fh)
        
        
#to get sum of prices of all products
with open("newprod.txt") as fh:
    s=0
    for line in fh:
        lst=line.split(":")
        s=s+int(lst[3])
    print("Sum: ",s)




