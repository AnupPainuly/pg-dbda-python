from abc import abstractmethod,ABC
class Person:
    def __init__(self,eid=0,nm="",mob=""):
        print("in Person constructor")
        self.__eid=eid
        self.__ename=nm
        self.__mob=mob
    def set_eid(self,eid):
        self.__eid=eid
    def get_eid(self):
        return self.__eid
    def set_ename(self,enm):
        self.__ename=enm
    def get_ename(self):
        return self.__ename
    def set_mob(self,m):
        self.__mob=m
    def get_mob(self):
        return self.__mob

    def __str__(self):
        return f"Id : {self.__eid} Name: {self.__ename} Mobile :{self.__mob}"
        
class Employee(Person,ABC):
    def __init__(self,eid=0,nm="",mob="",dept="",desg=""):
        super().__init__(eid,nm,mob)
        print("in Employee init")
        self.__dept=dept
        self.__desg=desg
    def set_dept(self,dt):
        self.__dept=dt
    def get_dept(self):
        return self.__dept
    def set_desg(self,ds):
        self.__desg=ds
    def get_desg(self):
        return self.__desg
    @abstractmethod
    def calcSal(self):
        pass

    def __str__(self):
       return super().__str__()+f" Department: {self.__dept} Designation: {self.__desg}"
        
class SalariedEmp(Employee):
    def __init__(self,eid=0,nm="",mob="",dept="",desg="",sal=""):
        super().__init__(eid,nm,mob,dept,desg)
        print("in salarieemp init")
        self.__sal=sal
        self.__bonus=round(0.10*sal,2)
    def set_sal(self,s):
        self.__sal=s
    def get_sal(self):
        return self.__sal
    def set_bonus(self,b):
        self.__bonus=b
    def get_bonus(self):
        return self.__bonus
    def getnewsofcompany(self):
        return "company profit grow by 50%"

    def __str__(self):
        return super().__str__()+f" Salary : {self.__sal}  Bonus: {self.__bonus:0.2f}"
    def calcSal(self):
        print("in SalariedEmp calculatesal")
        return self.__sal+0.10*self.__sal+0.12*self.__sal-0.08*self.__sal+self.__bonus

class ContractEmp(Employee):
    def __init__(self,eid=0,nm="",mob="",dept="",desg="",hrs=0,charges=0):
        super().__init__(eid,nm,mob,dept,desg)
        self.__hrs=hrs
        self.__charges=charges
    def set_hrs(self,h):
        self.__hrs=h
    def get_hrs(self):
        return self.__hrs
    def set_charges(self,charges):
        self.__charges=charges
    def get_charges(self):
        return self.__charges
    def getRules(self):
        return "there are 1 holiday in a month, otherwise it is cut of payment"
    def __str__(self):
        return super().__str__()+f" Hours: {self.__hrs} charges: {self.__charges}"
    def calcSal(self):
        print("in contract employee calculatesal")
        return self.__hrs*self.__charges

if __name__=="__main__":
    s=SalariedEmp(111,"xx",1111,"HR","mgr",1111)
    print(s)
    c=ContractEmp(112,"yy",2222,"admin","mgr",100,3000)
    print(c)





              
