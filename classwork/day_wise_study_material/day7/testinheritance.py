import sys
from inheritancedemo import *
emplist=[]
def addnewEmeployee(ch):
    eid=int(input("ente eid"))
    ename=input("enetr ename")
    mob=input("enetr mob")
    dept=input("enetr department")
    desg=input("enetr designation")
    if ch==1:
        sal=float(input("enter sal"))
        ob=SalariedEmp(eid,ename,mob,dept,desg,sal)
    elif ch==2:
        hrs=int(input("enter hours"))
        charges=float(input("enter charges"))
        ob=ContractEmp(eid,ename,mob,dept,desg,hrs,charges)
    emplist.append(ob)
def searchById(eid):
    for idx,ob in enumerate(emplist):
        if ob.get_eid()==eid:
            return idx,ob
    return -1,None
            
def getCalculatedSalary(eid):
    pos,ob=searchById(eid)
    if pos!=-1:
        return ob.calcSal()
    else:
        return -1
    
def displayall():
    for ob in emplist:
        print(ob)

def getnewsorrules(eid):
    pos,ob=searchById(eid)
    if pos!=-1:
        if isinstance(ob,SalariedEmp):
            return ob.getnewsofcompany()
        elif isinstance(ob,ContractEmp):
            return ob.getRules()
    else:
        return None
        

choice=0
while choice!=5:
    choice=int(input("""1. Add new Employee
    2. calculate Salary
    3. display all
    4. get news or rules from companyt
    5. exit
    choice:"""))
    match choice:
        case 1:
            ch=int(input("1. Salaried \n 2. Contract"))
            addnewEmeployee(ch)
        case 2:
            eid=int(input("enetr eid"))
            netsal=getCalculatedSalary(eid)
            if netsal!=-1:
                print("Salary : ",netsal)
        case 3:
            displayall()
        case 4:
            eid=int(input("enetr eid"))
            data=getnewsorrules(eid)
            if data!=None:
                print(data)
            else:
                print("Not found")
        case 5:
            #sys.exit(0)
            print("Thank you for visitig....")
    
