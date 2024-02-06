print("happy")

class superException(Exception):
    pass


while True:
    try:
        n=input("Enter the name without the character 'E' and 'e' in it: ")
        if "E" in n or"e" in n:
            raise superException()
        
    except superException:
        print("Please enter a name without E or e ")
    else:
        print("you have entered a name without E or e thankyou")
        break


# Note: The exception which is raised outside the try block cannot be handled with a except clause, example in the
# that is why try clause is a must  

