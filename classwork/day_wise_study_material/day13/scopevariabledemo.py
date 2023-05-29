# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:31:07 2021

@author: anilk
"""

#scope of variable

#local , global
#if you declare variables outside functions then it is global 
#otherwise it is local variable
lst=[]
def function1():
    #global count
    count=3
    lst.append("aaa") 
    print("in function:",count)
    count=count+1
    def function2():
        #global count
        #nonlocal count
        count=20
        print("in function2",count)
        
    function2()
    print("after calling function2: ",count)
    


count=1
count=count+1
function1()
print("count :",count)




def f1():
    global count
    count=0
    count=count+1
    print(count)
    #returtn count

    
count=0
count=f1()



