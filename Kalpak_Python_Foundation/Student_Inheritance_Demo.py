class Student:
    def info(self,rno,name):
        self.rno=rno
        self.name=name


class Exam(Student):
    def subject(self,cc,cg,cn):
        self.cc = cc
        self.cg = cg
        self.cn = cn


class Result(Exam):
    def res(self,):
        self.avg=(self.cc+self.cg+self.cn)/3

    def show(self):
        print("Roll no:",self.rno)
        print("Name:", self.name)
        print("Marks of CC:", self.cc)
        print("Marks of CG:", self.cg)
        print("Marks of CN:", self.cn)
        print("Average is:",self.avg)
        print("------------------------------")





Avg=Result()
Avg.info(1,"kalpak malpe")
Avg.subject(30,40,50)
Avg.res()
Avg.show()


Avg=Result()
Avg.info(12,"Mayur Kasture")
Avg.subject(20,40,40)
Avg.res()
Avg.show()