# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:49:04 2023

@author: anilk
"""
def division(num,num1):
    try:
        ans=num/num1
        return ans
    except ZeroDivisionError as e:
        print("number cannot be divide by zero")
        raise e
        
        
d={"a":100,"b":200}
for i in range(3):
    try:
        num=int(input("enetr number"))
        print(num)
        num1=int(input("enetr number"))
        print(num1)
        ans=division(num,num1)
        print("Answer: ",ans)
        k=input("enetr key")
        print(d[k])
        break
    except (ValueError,KeyError) as e:
        print("pls enetr number")
        print(e)
    except ZeroDivisionError:
        print("cannot divide by zero")
    except Exception as e:
        print("Error occured",e)
else:
    print("pls contact admin")
    
    
    
    
    