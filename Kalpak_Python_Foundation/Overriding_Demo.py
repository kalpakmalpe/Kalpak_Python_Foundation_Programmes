class parent:
    def show(self):
        print("i am parent..")

    def show(self):
        print("i am other...")

class child(parent):
    def show(self):
        print("i am child...")




p=parent()
p.show()


a=child()
a.show()


