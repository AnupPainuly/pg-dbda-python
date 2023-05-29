'''
#Q1. Reverse a given list in python
some_list=[100,200,300,400,500]
print(some_list)
some_list.reverse()
print(some_list)
'''

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

'''
#Q5. Given a two python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1=[10,20,30,40]
list2=[100,200,300,400]
#zip function returns tuple
for i in zip(list1,reversed(list2)):
        print(i)
'''

'''

#Q6. Remove empty strings from the list of strings
list1=["Ashish","","Athara","Amit","","Revati"]
for i in list1:
    if i=="":
        list1.remove("")
print(str(list1))

'''
'''

#Q7.Add item 7000 after 6000 in the following Python List 
#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
#output: 
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
list1[2][2].append(7000)
print(list1)

'''
'''

8.  Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look 
like the following list 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
Sub List to be added = ["h", "i", "j"] 
output: 
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'] 
              solution 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
subList = ["h", "i", "j"] 
 
list1[2][1][2].extend(subList) 
print(list1)

'''

'''
#9.  Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only 
#update the first occurrence of a value 
#list1 = [5, 10, 15, 20, 25, 50, 20] 
#output: 
#list1 = [5, 10, 15, 200, 25, 50, 20] 

list1=[5,10,15,20,25,50,20]
if 20 in list1:
    index=list1.index(20)
    list1[index]=200
    print(list1)

'''

'''
#Q10.Given a Python list, remove all occurrence of 20 from the list 

list1=[5,10,15,20,25,50,20]
list1=[i for i in list1 if i != 20]
print(list1)

'''
