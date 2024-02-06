class NL(Exception): # inheriting the exception class you can also use BASEEXCEPTION class too...
    pass
class checklevel():
    def NegativeLevel(self,a):
        self.level=a
        if self.level<0:
            raise NL() # raising the NL exception using raise keyword.
        else:
            print(f"You will enter level {self.level} shortely")

while True:
    b=int(input("Enter the level: "))
    abc=checklevel()
    try:
        abc.NegativeLevel(b)
    except NL:
        print("You have entered negative level please enter again")
    else: # The else block is used to execute a block of code if there is no exception in the try block.....
        break
    finally:  # The finally block is used to execute a block of code irrespective of exceptions in the try block before proceeding to the normal code.... 
        print("Thank you for executing this program..")

 

