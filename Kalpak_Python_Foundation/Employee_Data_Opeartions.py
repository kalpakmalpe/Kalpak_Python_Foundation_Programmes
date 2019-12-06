class Employee:

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def __str__(self):

        disp = ""

        disp += "Code: " + str(self.code) + " , Name : " + self.name + " , " + " Salary : " + str(self.salary)

        return disp


emp1 = Employee(101, "kapak", 40000)
emp2 = Employee(102, "mayur", 39000)
emp3 = Employee(103, "harshad", 50000)
emp4 = Employee(104, "sagar", 40000)
emp5 = Employee(105, "suyog", 45000)

emplist = [emp1, emp2, emp3, emp4, emp5]
print(type(emplist))


'''
#------ Employee Operations ------------------------------------------------------------------------------------------

def showEmployeeList():

    for emp in emplist:

        print(emp)


def searchEmployee(code):

    for emp in emplist:

        if emp.code == code:
            return emp

    return False

#-------------------------------------------------------------------------------------------------

print("Showing all employees...")
showEmployeeList()

print("Searching employee.....")
code = int(input("Enter code to search: "))
emp = searchEmployee(code);

if emp:
    print(emp)
else:
    print("Employee Not Found!")

'''