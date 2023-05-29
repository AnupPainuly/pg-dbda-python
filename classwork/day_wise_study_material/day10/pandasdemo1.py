# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:07:05 2023

@author: anilk
"""

import pandas as pd
df=pd.read_table("http://bit.ly/chiporders")
#to find column names
print(df.columns)
#to change the column names
#df.columns=["col1","col2","col3","col4","col5"]
print(df.columns)

#to find number of columns and rows
print(df.shape)
print(df.info())
#display first 5 lines
print(df.head())
print(df.head(12))

#display last few lines
print(df.tail())
print(df.tail(12))

#to find few lines
#display lines at index 1 to 6
#columns 2 onward
df.iloc[1:7,2:]

df.loc[1:7,['order_id',"item_name"]]

print(df.describe())

#to convert price into number
df['newprice']=df['item_price'].map(lambda x:x.replace("$",""))
df['intnewprice']=df['newprice'].astype('float')

print(df.info())
print(df['intnewprice'].sum())







