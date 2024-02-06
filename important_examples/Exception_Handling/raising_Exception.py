
a= int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

try:
    c=a/b
except ZeroDivisionError:
    print("Enter an integer not a zero")
else:
    print("The result of division is: " +str(c))




    