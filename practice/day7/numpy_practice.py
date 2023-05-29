#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[21]:


#One dimensional numpy array
a=np.array([1,2,3])
print(a)

#print shape which is row x column
print("row and columns of the array",a.shape)
#print dimension of the numpy array
print("dimension of the array",a.ndim)
print("datatype of the array ele",a.dtype)


# In[20]:


#Two dimensional numpy array
b=np.array([[1,2,3],[3,2,1]])
print(b)
print("row and columns of the array",b.shape)
print("dimension of the array",b.ndim)
print("datatype of the array ele",b.dtype)


# In[24]:


c=np.array([[[1,2,3],[4,5,6],[7,8,9]]],dtype='int16')
print(c)
print("row and columns of the array",c.shape)
print("dimension of the array",c.ndim)
print("datatype of the array ele",c.dtype)
print("size of element",c.itemsize)
print("size of array",c.size)


# In[35]:


d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
print("row and columns of the array",d.shape)
print("dimension of the array",d.ndim)
print("datatype of the array ele",d.dtype)
print("size of element",d.itemsize)
print("size of array",d.size)


# ## Accessing/Updating specific elements,rows,columns

# In[25]:


a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(a)
#getting specific elemetn [r,c]
a[1,3]


# In[26]:


#getting a specific row
a[0,:]


# In[27]:


#getting a specific column
a[:,2]


# In[28]:


#updating element
a[0,5]=1
print(a)


# ## Initializing the elements of array

# In[30]:


#Initializing with 2 rows and three columns all zeros
np.zeros((2,3))


# In[33]:


#Intializing with 2 rows and three columns all ones
np.ones((2,3), dtype='int32')


# In[34]:


#Init with any other number
np.full((2,2), 999)


# In[40]:


#Init with any number using already built shape.
np.full(c.shape,999)


# In[39]:


#Init with any number using already built shape.
np.full_like(c,999)


# In[44]:


#Init with random numbers
np.random.rand(4,2)


# In[45]:


#Init with random numbers using already built shape
np.random.random_sample(c.shape)


# In[57]:


#Init with random numbers (1-10) of integers values
np.random.randint(1,11,size=(3,3))


# In[58]:


#Init with indentity matrix
np.identity(5)


# In[73]:


#excercise for combining basic array inits
one_m=np.ones([5,5])
zero_m=np.zeros([3,3])
zero_m[1,1]=9
one_m[1:-1,1:-1]=zero_m
print(one_m)


# In[ ]:


## Statstics in numpy


# In[75]:


stats=np.array([[1,2,3],[4,5,6]])
stats


# In[79]:


#minimum in rows
np.min(stats,axis=1)


# In[80]:


#sum of whole array
np.sum(stats)


# In[82]:


#sum of columns
np.sum(stats,axis=0)


# In[84]:


#sum of rows
np.sum(stats,axis=1)

