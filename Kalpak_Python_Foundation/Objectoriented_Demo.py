#create the class Employee
class Employee:
    def accept(self,code,name,salary):
        self.code=code
        self.name=name
        self.salary=salary

    def display(self):
        print("Code:",self.code)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("------------------------------")


#crrete the object of emplyee
e=Employee()
e.accept("111","Mayur Kasture","50,000")
e.display()

e1=Employee()
e1.accept("112","Harshad Patil","50,000")
e1.display()
