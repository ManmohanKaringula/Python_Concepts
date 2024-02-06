# The __name__ is used in a situation where you want your program to act in a certain way when executed directly and act in
# a different way when the code is imported by another program.  


if __name__=="__main__":
    print(f'This line is executed when the moudule is runned directly and the name of the __name__ variable is: {__name__}')
else:
    print(f'This line is executed when the module is runned through importing the module and the name of the __name__ variable is: {__name__}')