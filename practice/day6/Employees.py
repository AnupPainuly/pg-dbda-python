class Employees:

    def __init__(self,first,last,pay) -> None:
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1=Employees("foo","bar",5000)
print(emp_1.email)
print(emp_1.fullname())
