# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:03:47 2023

@author: anilk
"""
import pandas as pd
dummy_data1 = {
        'id': ['1', '2', '3', '4', '5'],
        'Feature1': ['A', 'C', 'E', 'G', 'I'],
        'Feature2': ['B', 'D', 'F', 'H', 'J']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2']) 



dummy_data2 = {
        'id': ['1', '2', '6', '7', '8'],
        'Feature1': ['K', 'M', 'O', 'Q', 'S'],
        'Feature2': ['L', 'N', 'P', 'R', 'T']}
df2 = pd.DataFrame(dummy_data2, columns = ['id', 'Feature1', 'Feature2'])

df1['dept']='sales'
df2['dept']='purchase'

cframe=pd.concat([df1,df2],ignore_index=True)

dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}
df3 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])

mergeframe= pd.merge(cframe, df3,on='id',how="outer")

