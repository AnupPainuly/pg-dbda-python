'''
#Q1. Reverse a given list in python
some_list=[100,200,300,400,500]
print(some_list)
some_list.reverse()
print(some_list)
'''

#Q2. concatenate two lists index-wise

list1 = ["M", "na", "i", "Raj"] 
list2 = ["y", "me", "s", "esh"] 
concatenated_list=[]
for i in range(4):
    concatenated_list.append(list1[i] + list2[i])
#list comprehension with for loop
#concatenated_list=[list1[i]+list2[i] for i in range(min(len(list1),len(list2)))]
print(concatenated_list)

'''

#Q3. Given a python list of numbers. Turn every item in a list into its square
some_list=[1,2,3,4,5,6,7]
squared_list=[]
for i in some_list:
    squared_list.append(i**2)
print(squared_list)

'''

'''
#Q4. concatenate two lists in th following order:
list1 = ["Hello ", "Welcome "] 
list2 = ["Students", "Sir"]
#list comprehension with two nested loop
concatenated_list =[x+y+" " for x in list1 for y in list2]
print(concatenated_list)
'''
