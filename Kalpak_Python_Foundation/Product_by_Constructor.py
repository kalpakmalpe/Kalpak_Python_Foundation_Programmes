class Product:
    def __init__(self,sellcost,purchcost):
        self.sellcost=sellcost
        self.purchcost=purchcost

    def show(self):
        print("Sell cost is:",self.sellcost)
        print("purchase cost is:", self.purchcost)

    def compare(self):
         if (self.sellcost > self.purchcost) :
             print("product is in profit...")

         elif(self.sellcost==self.purchcost):
             print("neither loss nor cost....")


         else:
             print("product is in loss...")





pro=Product(200,100)
pro.show()
pro.compare()