'''
#Q1
string="stringy"
while True:
    print("***********************************************")
    print("1. display characters from even position      *")
    print("2. display characters from odd position       *")
    print("3. display length of a string                 *")
    print("4. add 'a' at the end of string length times  *")
    print("5. exit                                       *")
    print("***********************************************")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("even position char: ",end="")
            print(string[1::2])
        case 2:
            print("odd position char: ",end="")
            print(string[0::2])
        case 3:
            print("length of the string: ",end="")
            print(len(string))
        case 4:
            print(string.replace("stringy","stringy"+"a"*len(string)))
        case 5 :
            print("program terminated. Bye!")
            break
'''
'''
#Q2
input_string=str(input("enter some string: "))
sub=str(input("enter a substring: "))
pos=input_string.find(sub)
while pos != -1:
    print("postion: ",pos)
    pos=input_string.find(sub,pos+1)
print("Occurences of substring: ",input_string.count(sub))

'''
'''
#Q3
lst=[1,5,3,6,8,2,4]
while True:
    print("""1. add at last position
2. add at given position
3. Delete data by value
4. delete last element
5. delete from position
6. sort ascending
7. sort descending
8. reverse list
9. print in sorted order without changing orginal list
10. print in reverse order without changing original list
11. Display data normally
12. Display data numbered
13. exit""")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            lst.append(100)
        case 2:
            lst.insert(2,200)
        case 3:
            if 7 in lst:
                lst.remove(7)
            else:
                print("element not found")
        case 4:
            lst.pop()
        case 5:
            lst.pop(0)
        case 6:
            lst.sort()
        case 7:
            lst.sort(reverse=True)
        case 8:
            lst.reverse()
        case 9:
            print(lst)
        case 10:
            for i in sorted(lst):
                print(i,end=" ")
            print()
        case 11:
            for i in sorted(lst,reverse=True): 
                print(i,end=" ")
            print()
        case 12:
            for idx, i in enumerate(lst):
                print(idx,":",i)
        case 13:
            print("program terminated")
            break
'''

'''

#4. Create two lists to store cities and locations by accepting values from user.  
#Display 1st city and 1st location then 2nd city and 2nd location. 

city=[]
location=[]
for i in range(3):
    c=input("enter the city: ")
    city.append(c)
    l=input("enter the location: ")
    location.append(l)
for i in zip(city,location):
    print(i)
'''

'''
#Q5. Create a list and exchange the values as index and index as values. 
#lst=[12, 1, 3, 7, 8, 5, 8] 
#         0   1  2  3  4  5   6 
#Output should be as follows. 
#lst1=[-1 ,1, -1, 2, -1, 5, -1, 3, 6, -1, -1, -1, 0]

lst = [12, 1, 3, 7, 8, 5, 8]
lst1 = [-1] * (max(lst)+1) 
for index, val in enumerate(lst):
    lst1[val]=index
print(lst1)
'''

'''
6. Write a menu driven program to practice Set functions.  
Write a program to accept names from users and store it in a set. 
Display the following menu: 
print("""1. delete element if exists otherwise 
      do not show any errr""") 
print("2. add a elemet") 
print("3. create one more set") 
print("4. union of 2 sets") 
print("4. intersection of 2 sets") 
print("5. difference of 2 sets") 
print("6. convert set into frozenset") 
print("6. exit")
'''

'''
#Q6

set1=set() #can not use curly braces since dictionary also uses curly braces
for i in range(3):
    name=input("enter the name: ")
    set1.add(name)
print(set1)

def createset():
    set2=set()
    for i in range(3):
        name=input("enter the name: ")
        set2.add(name)
    return set2
    #print("succefully created",set2)

def addele():
    name=input("enter the name to add in the set1: ")
    set1.add(name)
    print("element added succesfully",set1)

def discardele():
    name=input("enter the name to be discarded: ")
    set1.discard(name)
    return set1
    #print("element discarded succesfully",set1)

def union_sets():
    set2=createset()
    #u_sets=set1.union(set2)
    u_sets=set1|set2
    print("union_sets of set and set2",u_sets)

def intersection_sets():
    set2=createset()
    #i_sets=set1.intersection(set2)
    i_sets=set1&set2
    print("intersection of set and set2: ",i_sets)

def diff_sets():
    set2=createset()
    d_sets=set1-set2
    print(d_sets)

def freeze_set(set1):
    fs=frozenset(set1)
    print(type(fs))
    print(fs)



while True:
    print("""1. delete element if exists otherwise 
do not show any errror.
2. add a elemet") 
3. create one more set") 
4. union of 2 sets") 
4. intersection of 2 sets") 
5. difference of 2 sets") 
6. convert set into frozenset") 
6. exit""")
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            discardele()
        case 2:
            addele()
        case 3:
            set2=createset()
            print("succefully created",set2)
        case 4:
            union_sets()
        case 5:
            intersection_sets()
        case 6:
            diff_sets()
        case 7:
            freeze_set(set1)
        case 8:
            print("program terminated")
            break
        case _:
            print("Invalid Choice")
'''

'''
#Q7.
#User
#Generate a list of lists (NOTE: List should get generated dynamically) 
#Accept a 6 values from user and check last digit of the each number. 
#If it is 1 then add it in the list at 1st position. 
#If 0 then it should get added at list in 0th position. 
#e.g list should look as follows 
#[[10],[51],[52]] 
#[[10,30,20,40],[11,31,41,31],[22,32,42]....] 
# 
#if user enters 15 then the resultant list should be 
# 
#[[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]]
def generate_list_of_lists(numbers):
    result = [[] for _ in range(10)]
    for number in numbers:
        last_digit = number % 10
        if last_digit == 0:
            result[0].append(number)
        else:
            result[last_digit].append(number)
    return result

numbers = []
for i in range(6):
    number = int(input("Enter a number: "))
    numbers.append(number)
list_of_lists = generate_list_of_lists(numbers)
print(list_of_lists)
'''

'''
#Q8
def add_string_in_order(string, strings_list):
    second_character = string[1]
    index = -1
    
    for i, s in enumerate(strings_list):
        if len(s) > 1 and s[1] == second_character:
            index = i
            break
    
    if index != -1:
        strings_list.insert(index, string)
    else:
        strings_list.append(string)

strings_list = ["dxz", "axz", "bat", "rat", "cat", "pat", "bbc", "bbm", "cbm"]
new_string = input("Enter a string: ")
add_string_in_order(new_string, strings_list)
print(strings_list)
'''
