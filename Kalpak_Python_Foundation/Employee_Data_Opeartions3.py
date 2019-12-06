class employee:
    def __init__(self,code,name,salary):
        self.code=code
        self.name=name
        self.salary=salary


class emplst(employee):


    def show(self):
        print("code:",self.code)
        print("name:",self.name)
        print("salary:",self.salary)


    def list(self):
        lst=(self.code,self.name,self.salary)
        print(lst)





e=emplst(101,"kalpak",30000)
e.show()
e.list()