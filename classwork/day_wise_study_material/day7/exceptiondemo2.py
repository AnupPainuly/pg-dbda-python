# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:11:58 2023

@author: anilk
"""
class WrongWordChoice(Exception):
    def __init__(self,msg:"error occured"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
    
word="enjoy"
while True:
    try:
        wrd=input("enetr word")
        if word==wrd:
            print("yepee! you got the answer")
            break
        else:
            raise  WrongWordChoice("Oops! you lost the chance, pls try again")
    except WrongWordChoice as e:
        print(e)
        
        
try:
   fh=open("test,txt")
   #use the file
   
except:
    print("error")
finally:
    print("in finally block")
    fh.close()
        
        
        
        
        
