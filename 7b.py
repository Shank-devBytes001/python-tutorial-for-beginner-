class employee:
    def __init__(self):
        self.name=""
        self.empid=""
        self.dept=""
        self.sal=0

    def getempdt(self):
        self.name=input("enter the name")
        self.empid=input("enter the employee id")
        self.dept=("enter the department:")
        self.sal=int(input("enter the salary"))

    def showdt(self):
        print("enter the employee details")
        print("name=",self.name)
        print("empid=",self.empid)
        print("department=",self.dept)
        print("salary=",self.sal)

    def upsal(self):
        self.salary=int(input("enter the new salary="))
        print("the new salary is:",self.sal)


e1=employee()
e1.getempdt()
e1.showdt()
e1.upsal()
                        
