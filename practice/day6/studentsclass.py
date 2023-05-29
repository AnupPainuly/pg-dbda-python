class Students:
    def __init__(self,student_id,name,marks) -> None:
        #private member of the class starts with dunder
        self.__student_id=student_id
        self.__name=name
        self.__marks=marks

        #setter methods
    def set_student_id(self,student_id):
        self.__student_id=student_id

    def set_name(self,name):
        self.__name=name

    def set_marks(self,marks):
        self.__marks=marks

    #getter methods
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    #to string equivalent

    def __str__(self):
        return f"id:{self.__student_id} Name:{self.__name} Marks:{self.__marks}"

if __name__=="__main__":
    obj=Students(12,"foo",41)
    print(obj)
