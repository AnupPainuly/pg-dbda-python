# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:40:10 2023

@author: anilk
"""

import pandas as pd
df=pd.read_table('empdata.dat',sep=":",header=None)
df.columns=['empid','ename','desg','sal','dept']
g=df.groupby('dept')
for dept,data in g:
    print("Department : ",dept)
    print(data)

hrdf=g.get_group("HR")

print(g.sum())

#to find how many times a particular value appears 
#in the data frame
data=df['dept'].value_counts()
print(type(data))

import matplotlib.pyplot as plt

x=data.index
print(x)

y=data.values
print(y)

plt.bar(x,y)
plt.xlabel("Department name")
plt.ylabel("emp count")
plt.title("Employee-dept data")
#plt.grid()
plt.show()










