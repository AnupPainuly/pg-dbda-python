#!/usr/bin/env python
# coding: utf-8

# # EDA for Iris Dataset

# ## Importing the required libraries

# In[3]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


# ## Loading data set

# In[4]:


iris=pd.read_csv('Iris.csv')
#remove unwanted part from a column
iris['Species'] = iris['Species'].str.replace(r'Iris-', '')
iris


# ## Structural information about the data

# In[5]:


iris.info()


# ## Data Insights:
# * No null entries
# * Only one categorical column

# In[45]:


iris.describe()


# In[46]:


iris.groupby('Species').agg(['mean','median'])


# ## check for duplication

# In[7]:


iris[iris.duplicated()]


# ## Balance check

# In[8]:


iris['Species'].value_counts()


# In[9]:


# countplot() method is used to Show the counts of observations in each categorical bin using bars
#sns.countplot(iris['Species']) # this gives an ValueError as it is trying to plot categoical value on y axis
sns.countplot(data=iris,x='Species')
plt.title('Species Count')


# ## Scatter plot for species wise sepal length and sepal width

# In[10]:


sns.scatterplot(data=iris, x='SepalLengthCm', y='SepalWidthCm',hue='Species') #hue parameter determines which column in the data frame should be used for colour encoding.
#c='Species' taked sequence of numbers,colors or color
plt.title("Scatter Plot sepal length v/s sepal width for each Species")
plt.style.use('ggplot')


# ## Scatterplot Observations: 
# 1. setosa species has larger sepal width as compared to sepal length.
# 1. virginica species has larger sepal length in contrast to the sepal width.

# ## Scatter plor for species wise petal length and petal width.

# In[15]:


sns.scatterplot(data=iris, x='PetalLengthCm',y='PetalWidthCm',hue='Species')
plt.title("Scatter plot petal length vs petal width")
plt.style.use('ggplot')


# ## Scatter plot obeservation:
# 1. setosa species have smallest petal length and width.
# 2. virginica species has largest petal length and width while versicolor lie in middle of the other two.

# In[28]:


cols_to_plot = iris.columns[1:6].tolist() # explicitly add the column "Outcome" to your list of columns to plot
sns.pairplot(iris[cols_to_plot], hue='Species')


# ## checking correlation

# In[40]:


#plt.figure(figsize=(10,11))
col_for_corr=iris.columns[1:5].tolist()
sns.heatmap(iris[col_for_corr].corr(),annot=True)
plt.style.use('ggplot')
plt.plot()


# In[70]:


fig,axes=plt.subplots(2,2,figsize=(9,9)) #defining the canvas by variable fig and axes with axes.
sns.boxplot(data=iris,y='PetalLengthCm',x='Species',orient='v',ax=axes[0,0])
sns.boxplot(data=iris, x='Species',y='PetalWidthCm',ax=axes[0,1])
sns.boxplot(data=iris, x='Species',y='SepalWidthCm',ax=axes[1,0])
sns.boxplot(data=iris, x='Species',y='SepalLengthCm',ax=axes[1,1])
plt.style.use('ggplot')


# ## Density of distribution across length and width

# In[79]:


#The names ax and pluralized axs are preferred over axes because for the latter it's not clear if it refers to a single Axes instance or a collection of these.
fig, axs=plt.subplots(2,2,figsize=(16,9))
sns.violinplot(data=iris,x='Species',y='PetalLengthCm',orient='v',ax=axs[0,0],inner='quartile')
sns.violinplot(data=iris,x='Species',y='SepalLengthCm',orient='v',ax=axs[0,1],inner='quartile')
sns.violinplot(data=iris,x='Species',y='PetalWidthCm',orient='v',ax=axs[1,0],inner='quartile')
sns.violinplot(data=iris,x='Species',y='PetalWidthCm',orient='v',ax=axs[1,1],inner='quartile')
plt.style.use('ggplot')

