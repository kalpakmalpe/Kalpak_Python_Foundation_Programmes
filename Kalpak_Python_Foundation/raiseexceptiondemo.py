class NotAllowed(Exception):

    def __init__(self,msg):
        super(NotAllowed,self).__init__(msg)


num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))

try:
    if (num1<num2):
        raise NotAllowed("Division not allowed...")

    div=num1/num2
    print("Division is:",div)


except NotAllowed as e:
    print(e)

except ZeroDivisionError as e:
    print(e.__class__,":",e)


else:
    print("Division is completed....")