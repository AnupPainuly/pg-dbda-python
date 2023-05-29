# -*- coding: utf-8 -*-
"""
Created on Sun May 21 09:06:12 2023

@author: anilk
"""
import os
d={}
if os.path.exists("empdata.dat"):
    with open("empdata.dat") as fh:
        for line in fh:
            lst=line.rstrip('\n').split(":")
            print(lst)
            try:
                d[lst[4]]=d[lst[4]]+int(lst[3])
            except KeyError:
                d[lst[4]]=int(lst[3])
            
import os
d={}
if os.path.exists("empdata.dat"):
    with open("empdata.dat") as fh:
        for line in fh:
            lst=line.rstrip('\n').split(":")
            print(lst) 
            #['444', 'Ashwini', 'analyst', '5555', 'HR\n']
            v=d.get(lst[4],-1)
            if v==-1:
               dept=lst[4]
               sal=int(lst[3])
               #if key does not exists add it and assign salary to it
               d[dept]=int(sal)  
            else:
                dept=lst[4]
                sal=int(lst[3])
                #if key does not exists add it and assign salary to it
                d[dept]=d[dept]+sal 
            print(d)            
            
            
            
    