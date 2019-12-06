


square=(map(lambda x:x**2  ,[1,2,3,4,5,6,7,8,9]))
for s in square:
    if  s%2==0:
        print(s)



def word(x):
    if x==0:
        print("Zero")
    elif x==1:
        print("One")
    elif x==2:
        print("Two")
    elif x==3:
        print("Three")
    elif x==4:
        print("Four")
    elif x==5:
        print("Five")

    return x


words = list(map(word,[1,2,3,4]))
print(words)
