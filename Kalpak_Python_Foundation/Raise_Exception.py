#Raise Expression Demonstration


class NotSame(Exception):
    def __init__(self,msg):
        super(NotSame,self).__init__(msg)


str1=input("Enter str1:")
str2=input("Enter str2:")


try:
    if(str1 != str2):
        raise NotSame("string is not matching...")

    str=str1+str2
    print("New string is:",str)


except NotSame as n:
    print(n)


else:
    print("operation is completed....")
