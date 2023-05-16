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
