def show(st=str(input("Enter the string:"))):
    print("Current string is:",st)

def create():
    fp=open("a.txt","r")
    str=fp.read()
    fp.close()