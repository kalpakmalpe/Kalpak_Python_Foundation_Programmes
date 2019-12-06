#Decorator Demo

def newdemo(func):


    def inner():

        print("Before Modify")
        func()
        print("After Modify")

    return inner


@newdemo
def demo():
    print("This Is Demo Function..")


demo()
