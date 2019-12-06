
num1= int(input("enter number1:"))
num2= int(input("enter number2:"))



try:
    div=num1/num2
    print("division is:",div)

except ZeroDivisionError:
    print("Division error...")


#try:
#   sum=num1+num2
#   print("sum is:",sum)

except NameError:
    print("Invalid name...")

else:
    print("Division occured")

sum=num1+num2
print("sum is:",sum)






