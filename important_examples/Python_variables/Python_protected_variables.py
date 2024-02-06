# PROTECTED VARIABLES
# The protected variables can be used among the class and its sub class but not outsite the class and sub classes like 
# classes 
class sup():
    _u=322

    def __init__(self):
        self._a=12

    def rrp(self):
        print(f"The protected value is {self._a}")

class der(sup):
    def uu(self):
        print(f"The protected variabels are {self._a}")

class rrt():
    def tty(self):
        print(f"The protected variables are {self._a}")


obj1=sup()
obj1.rrp()
obj2=der()
obj2.uu()

#obj3=rrt()
#obj3.tty()
# the above two lines of code raise AttributeError because the class rrt is not a sub_class of class sup() 

# The python interpreter has nothing to do with _a (Single_Underscore Variable) it is just a convention to follow 

print(sup._u)