# PRIVATE VARIABELS
# the private variables can be accessed only with in the class SYNTAX: __VariableName
class sip():
    def __init__(self):
        self.__a=20

    def somemethod(self):
        print(f"The private variables can accessed in the same class {self.__a}") # the variable is accessed in the class

class uup(sip):
    def iip(self):
        print(f"The private variables are {self.__a}")


obj1=sip()
obj1.somemethod()

# The following syntax would raise an AttributeError since the private variables (__a) cannot be accessed outside the class 
# error syntax:
#              print(tdf.__a)  <<<--------------- IMPORTANT  ERROR XXXXXXX

# But the private variables are just the convention there are no private variables in python. The mechanish behind private
# variables is that the __VariableName is changed to  Objectname._classname__VariableName
# The above concept is known as NAME_MANGLING

print(obj1._sip__a)       # As you can see it worked

obj2=uup()
obj2.iip() #--> raises AttributeError since the __a variabel is a private variable 
