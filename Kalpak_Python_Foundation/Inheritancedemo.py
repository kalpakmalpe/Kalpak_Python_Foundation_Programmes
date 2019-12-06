class Addition:
    def add(self,a,b):
        print("Addition is:",a+b)


class Subtraction(Addition):
    def sub(self,a,b):
        print("Subtraction is:",a-b)



class Multiplicaton:
    def mult(self,a,b):
        print("Multiplication is:",a*b)


class Devision(Multiplicaton):
    def dev(self,a,b):
        print("Devision is:",a/b)


class Mathematics(Subtraction,Devision):
    print()






math=Mathematics()
math.mult(2,2)
math.sub(2,2)
math.add(2,2)
math.dev(2,2)
