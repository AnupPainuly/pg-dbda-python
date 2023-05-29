class Student:
    def __init__(self,sid=0,nm="",m1=0,m2=0,m3=0):
        self.__sid=sid
        self.__sname=nm
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
    #setter methods
    def set_sid(self,sid):
        self.__sid=sid
    def get_sid(self):
        return self.__sid
    def set_sname(self,snm):
        self.__sname=snm
    def get_sname(self):
        return self.__sname
    def set_m1(self,m1):
        self.__m1=m1
    def get_m1(self):
        return self.__m1
    def set_m2(self,m2):
        self.__m2=m2
    def get_m2(self):
        return self.__m2
    def set_m3(self,m3):
        self.__m3=m3
    def get_m3(self):
        return self.__m3
    def calculatePercent(self):
        return ((self.__m1+self.__m2+self.__m3)/180)*100
    def __str__(self):
        return f"Id: {self.__sid} Name:{self.__sname} Marks:{self.__m1},{self.__m2},{self.__m3}"

if __name__=="__main__":
    ob=Student(12,'Ashish',34,45,56)
    print(ob)
    ob1=Student(13,'Soha',45,55,47)
    print(ob1)
