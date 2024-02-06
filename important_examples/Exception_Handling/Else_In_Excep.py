# In the below code if the exception is raised and the try block does not execute completely and the exception is handled.
while True:
    try:
        a=int(input("Enter the input:  "))
        break
    except ValueError:
        print("The entered value is not valid")
    
# The code below is similar to the above code except the try suite is smaller the break statement in else gets executed when exception 
# does'nt rise 

while True:
    try:
        a=int(input("Enter the input:  "))
    except ValueError:
        print("The entered value is not valid")
    else:
        break

# the else suite after the except block gets executed if there is no exception raised 
# it is better to use the else to make the try suite small and convenient

# NOTE: The use of the else clause is better than adding additional code to the try clause because it avoids accidentally 
# catching an exception that wasn't raised by the code being protected by the try ... except statement.