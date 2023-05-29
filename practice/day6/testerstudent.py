from studentsclass import *
stu_list=[Students(1,"asdf",43),Students(2,"lkjh",31)]
def addnewStudent():
    student_id=int(input("enter student id: "))
    name=input("enter name of the student id: ")
    marks=int(input("enter marks for the student id: "))
    obj=Students(student_id,name,marks)
    stu_list.append(obj)

def displayall():
    for obj in stu_list:
        print(obj)

def searchbyid(s_id):
    for idx,obj in enumerate(stu_list):
        if obj.get_student_id()==s_id:
            return idx,obj
    return -1,None #return -1 for index and None for obj

def displaybyid(s_id):
    pos,obj=searchbyid(s_id)
    if pos!=-1:
        print(obj)
    else:
        print("Not found")

while True:
    choice=int(input("""1. add new student
    2. delete student
    3. modify student
    4. display student by id
    5. display all
    6. display by marks
    7. exit
    choice:  """))
    match choice:
        case 1:
            addnewStudent()
        case 4:
            s_id=int(input("enter the student id to search for: "))
            displaybyid(s_id)
        case 5:
            displayall()
        case _:
            print("Invalid choice")
