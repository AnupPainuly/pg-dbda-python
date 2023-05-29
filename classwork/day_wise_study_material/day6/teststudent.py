from studentclass import *
choice=0
slist=[Student(1,'Ashu',55,55,56),Student(2,"Ajinkya",45,44,55)]
def addnewStudent():
    sid=int(input("enetr sid"))
    snm=input("enter name")
    m1=int(input("enter marks1"))
    m2=int(input("enter marks2"))
    m3=int(input("enter marks3"))
    ob=Student(sid,snm,m1,m2,m3)
    slist.append(ob)
    
def searchbyID(sid):
    for idx,ob in enumerate(slist):
        if ob.get_sid()==sid:
            return idx,ob
    return -1,None

def updateById(sid,m1,m2,m3):
    pos,ob=searchbyID(sid)
    if pos!=-1:
        ans=input(f"Id : {ob.get_sid()} name:{ob.get_sname()}(y/n)?") #Pyright : Ignore reportOptionalMemberAcess
        if ans=="y":
            ob.set_m1(m1)
            ob.set_m2(m2)
            ob.set_m3(m3)
            return 1
        else:
            return 2
    else:
        return 3
def deletebyId(sid):
    idx,ob=searchbyID(sid)
    if idx!=-1:
        ans=input(f"Id : {ob.get_sid()} name:{ob.get_sname()}(y/n)?")
        if ans=="y":
            slist.pop(idx)
            return 1
        else:
            return 2
    else:
        return 3
        
def displaybyID(sid):
    pos,ob=searchbyID(sid)
    if pos!=-1:
        print(ob)
    else:
        print("not found")
def displayall():
    for ob in slist:
        print(ob)
def displaybymarks(mrk):
    for ob in slist:
        if ob.get_m1()>mrk:
            print(ob)
        
while choice!=7:
    choice=int(input("""1. add new student
    2. delete student
    3. modify student
    4. display student by id
    5. display all
    6. display by marks
    7. exit
    choice: """))
    match choice:
        case 1:
            addnewStudent()
        case 2:
             sid=int(input("enetr student id to delete"))
             status=deletebyId(sid)
             if status==1:
                print("deleted successfully")
             elif status==2:
                print("found but not modified")
             else:
                print("not found")
        case 3:
            sid=int(input("enetr student id"))
            m1=int(input("enetr marks m1"))
            m2=int(input("enetr marks m2"))
            m3=int(input("enetr marks m3"))
            status=updateById(sid,m1,m2,m3)
            if status==1:
                print("modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("not found")
                
            
        case 4:
            sid=int(input("enetr student id"))
            displaybyID(sid)
        case 5:
            displayall()
        case 6:
            mrk=int(input("enter marks for display"))
            displaybymarks(mrk)
        case 7:
            print("Thank you for visiting....")
        case _:
            print("wrong choice")      
