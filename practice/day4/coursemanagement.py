#course management system
courses={"DBDA":57,"DAI":50}

#function to add a course
def addnewcourse():
    course_name=input("enter new course name =>").upper()
    students=int(input("enter number of students =>"))
    #get method returns default value when key not found in the dictionary. which is set to -1 in the below line.
    v=courses.get(course_name,-1)
    print(v)
    if v==-1:
        courses[course_name]=students
        return True
    else:
        return False

#function to delete a course
def deletecourse():
    course_name=input("enter course to be deleted =>").upper()
    v=courses.get(course_name,-1)
    if v!=-1:
        ans=input(f"{course_name} --> {v} type (y/n) for deleting =>")
        if ans=="y":
            #deletes key-value pair if exists
            courses.pop(course_name)
            return 1 #found the key and deleted the key-value pair
        else:
            return 2 #found the key but did not delete the key-value pair
    else:
        return 3 #key not found in the dictionary

#function to display the dictionary
def displayall():
    #item method returns key-value in form a tuple
    for k,v in courses.items():
        print(f"{k}-->{v}")

#function to modify the value of a key
def mod_students():
    course_name=input("enter the course name to modify students for =>").upper()
    students=int(input("enter the new no of students =>"))
    v=courses.get(course_name,-1)
    if v!=-1:
        ans=input(f"no of students of {course_name} having --> {v} will be modified to {students} (y/n) =>")
        if ans=="y":
            #there is no specific method to modify the value.
            #the below line overwrites the previous value
            courses[course_name]=students
            return 1
        else:
            return 2
    else:
        return 3

def mod_coursename():
    course_name=input("enter the course name => ").upper()
    new_course_name=input("enter new course name =>").upper()
    v=courses.get(course_name,-1)
    if v!=-1:
        ans=input(f"modify {course_name} to {new_course_name} (y/n)?")
        if ans=="y":
            old_val=courses.pop(course_name)
            courses[new_course_name]=old_val
            return 1
        else:
            return 2
    else:
        return 3

#search the dictionary by the key and retreive key-value pair
def course_by_name():
    course_name=input("enter the course name => ")
    for k,v in courses.items():
        if k==course_name:
            print(f"{k}-->{v}")
            
            
while True:
    choice=int(input("""
    __________________________________________________________
   | 1. add a new course                                      |
   | 2. delete a course                                       |
   | 3. modify number of participants                         |
   | 4. modify the course name                                |
   | 5. display all courses with number of participants > 40  |
   | 6. display all courses                                   |
   | 7. display a particular course                           | 
   | 8. exit                                                  |
   |__________________________________________________________|
    choice => """))
    match choice:
        case 1:
            if (addnewcourse()):
                print("course added succesfully")
            else:
                print("duplicate course")
        case 2:
            if(deletecourse()==1):
                print("succesfully deleted")
            elif(deletecourse()==2):
                print("modification aborted")
            else:
                print("key not found")
        case 3:
            if (mod_students()==1):
                print("capacity succesfully modified")
            elif(mod_students==2):
                print("modification aborted")
            else:
                print("Invalid course name provided")
        case 4:
            if (mod_coursename()==1):
                print("course name modified")
            elif (mod_coursename()==2):
                print("modification aborted")
            else:
                print("Invalid course name")

        case 6:
            displayall()
        case 7:
            course_by_name()
        case 8:
            print("program terminated")
            break
