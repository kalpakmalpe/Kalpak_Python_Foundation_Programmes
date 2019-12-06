import employees as f


print("Showing all employees...")
f.showEmployeeList()

print("Searching employee.....")
code = int(input("Enter code to search: "))
emp = f.searchEmployee(code)

if emp:
    print(emp)
else:
    print("Employee Not Found!")



emp=f.highest()
print("Employee with highest salary:")
print(emp)





code=int(input("Enter the code which to be remove:"))
isDeleted=f.removebyid(code)

if isDeleted:
    print("Employess deleted successfully.......")
else:
    print("Unable to deleted...")





f.showEmployeeList()


f.addtion()

print("add the new employee:")
empn=(106,"kalpak",1200)