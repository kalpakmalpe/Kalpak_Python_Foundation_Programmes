import employee as a


def showEmployeeList():

    for emp in a.emplist:

        print(emp)


def searchEmployee(code):

    for emp in a.emplist:

        if emp.code == code:
            return emp

    return False





def highest():
    maxsalary=0
    maxemp=""

    for emp in a.emplist:
       if emp.salary > maxsalary:
            maxsalary = emp.salary
            maxemp=emp


    return maxemp





def removebyid(code):
    i=0
    for emp in a.emplist:
        if emp.code==code:
            del a.emplist[i]
            return True

        i+=1

    return False






def addtion(code,name,salary):
    empn=a.emplist(a.code,a.name,a.salary)
    a.emplist.append(empn)

