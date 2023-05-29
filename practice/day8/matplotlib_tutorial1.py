#!/usr/bin/env python
# coding: utf-8

# In[55]:


from matplotlib import pyplot as plt
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x,dev_y)
plt.xlabel("Ages")
plt.ylabel("salary")
plt.title("Median Salary for devs by age")


# In[56]:


#line plot
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, 'k--', label="All Devs") # k is for color black and -- for dashed line
plt.plot(ages_x, dev_y, 'b', label="Py Devs") # b is for blue color
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Median Salary for Python Devs")
plt.legend()


# In[57]:


py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 
         62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, py_dev_y, color='k', linestyle='--', marker='o', label="All Devs")
plt.plot(ages_x, dev_y, color='b', marker='.', label="Py Devs")
plt.plot(ages_x, js_dev_y,color='magenta', marker='.',label="Js Devs")
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Median Salary for Python Devs")
plt.legend()
plt.grid()


# In[51]:


#built in style
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 
         62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, py_dev_y, linestyle='--', marker='o', label="All Devs")
plt.plot(ages_x, dev_y, marker='.', label="Py Devs")
plt.plot(ages_x, js_dev_y, marker='.',label="Js Devs")
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Median Salary for Python Devs")
plt.legend()
plt.style.use('fivethirtyeight')

