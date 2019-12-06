
#create class media
class Media:
    #accept the code and price of book
    def getinfo(self):
        self.code=int(input("Enter the code:"))
        self.price=int(input("Enter the price:"))

#create class ebook
class ebook(Media):
    # accept the title and size
    def getebook(self):
        self.title=input("Enter the title e-book:")
        self.size=input("Enter the size of e-book:")

#create class magzine
class magzine(Media):
    #accept the author and publication
      def getmag(self,):
          self.author=input("Enter the Author:")
          self.publication=input("Enter the Publication:")


#create class sale
class sale(magzine,ebook):
    #accept sellcost
    def getsale(self):
        self.sellcost=int(input("Enter the Sellcost:"))
        print("=======================================")



#display the output
    def show(self):
        print("Code:",self.code)
        print("Price:",self.price)
        print("title of ebook:",self.title)
        print("size of ebook:",self.size)
        print("author:",self.author)
        print("publication:",self.publication)
        print("sellcost:",self.sellcost)

        #compare sellcost and price
        if (self.sellcost > self.price):
            print("product is in profit.....")

        elif(self.sellcost==self.price):
            print("No profit........")

        else:
            print("product is in loss......")


        print("---------------------------------")


book=sale()
book.getinfo()
book.getebook()
book.getmag()
book.getsale()
book.show()


