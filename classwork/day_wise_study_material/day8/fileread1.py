# -*- coding: utf-8 -*-
"""
Created on Sun May 21 08:55:40 2023

@author: anilk
"""

#open the file
try:
    fh=open("empdata.dat")
    fh1=open("empdatacopy.txt","a")
    for line in fh:
        print(line.rstrip('\n'))
        fh1.write(line)
except FileNotFoundError:
    print("file does not exists")
finally:
    fh.close()
    fh1.close()
    
    
    
    
    
    
    
    