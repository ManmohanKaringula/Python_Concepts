# There is a method to add a function into to a object or a class dynamically to be precise we can add the function which is declared 
# outside the class into a class....
from types import MethodType
# First method: here we will store the reference of a function into the a object reference
class student:
    def __init__(self, rn):
        self.rn=rn

def display(x):
    print(f"Helloworld the number is {x}")

obj1=student(101)
obj1.display=display
obj1.display(5) # Here the reference is not the complete binding of the function into the class 

# Here we will try to create a instance method out of the class and see
def displayRollno(self):
    print(f"The roll number of the student is {self.rn}")

# obj1.displayRollno=displayRollno
# obj1.displayRollno()

# The above two line still give an error about the positional arguments ie.., self

# To dynamically add a method to a object we use the MethodType() function which is imported from the tyeps module in python
# The MethodType will add bind the method to an instance(Object) and form a bound method 

obj1.displayRollno=MethodType(displayRollno, obj1) # Remember that this method will only bind the displayRollno to the
# instance of the object not to the class
obj1.displayRollno()
# If we try to create another instance object using the same class (student) we dont get the displayRollno method for that 
# perticular instance....
 
