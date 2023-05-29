#course management system
courses={"DBDA":57,"DAI":50}

def addnewcourse():
    cname=input("enter new coursename")
    num=int(input("enter number of participants"))
    v=courses.get(cname,-1)
    print(v)
    if v==-1:
        courses[cname]=num
        return True
    else:
        return False
def deletecourse(cname):
    v=courses.get(cname,-1)
    if v!=-1:
        ans=input(f"{cname} --> {v} delete (y/n)")
        if ans=="y":
            courses.pop(cname)
            return 1
        else:
            return 2
    else:
        return 3

def modifynumber(cname,num):
    v=courses.get(cname,-1)
    if v!=-1:
        ans=input(f"{cname} --> {v} modify {num}(y/n)")
        if ans=="y":
            #overwrite the value of the key
            courses[cname]=num
            return 1
        else:
            return 2
    else:
        return 3    
def modifyname(cname,newcname):
    v=courses.get(cname,-1)
    if v!=-1:   #DBDA:57      eDBDA:57
        ans=input(f"modify {cname} to {newcname} (y/n)?")
        if ans=="y":
            #delete course cname and returns its value
            val=courses.pop(cname)
            #add a new key and value pair
            courses[newcname]=val
            return 1
        else:
            return 2
    else:
        return 3
            
def displaybyNum(num):
    for k,v in courses.items():
        if v>num:
            print(f"{k}---->{v}")
    
def displayall():
    for k,v in courses.items():
        print(f"{k}---->{v}")
    
choice=0
while choice!=8:
    choice=int(input("""
    1. add new course
    2. delete the couse
    3. modify number of participants
    4. mofdify course name
    5. display all courses with number of participants are > 40
    6. display all courses
    7. display a particular course
    8. exit
    choice:
    """))
    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("added successfully")
            else:
                print("duplicate course")
        case 2:
            cname=input("enter coursename to delete")
            status=deletecourse(cname)
            if status==1:
                print("deleted successfully")
            elif status==2:
                print("found but not deleted")
            else:
                print("course not found")
        case 3:
             cname=input("enter coursename to modify participants")
             num=int(input("enter number of participants"))
             status=modifynumber(cname,num)
             if status==1:
                print("modified successfully")
             elif status==2:
                print("found but not modifies")
             else:
                print("course not found")
        case 4:
            cname=input("enter coursename to modify participants")
            newcname=input("enter coursename to modify participants")
            status=modifyname(cname,newcname)
            if status==1:
                print("modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("course not found")
        case 5:
            num=int(input("enter number of participants"))
            displaybyNum(num)
        case 6:
            displayall()
        case 8:
            print("Thank for visiting.....")
        case _:
            print("wrong choice")
