# Adding class methods (unbound methods) to a class is similar to adding bound methods that is using MethodType  

from types import MethodType
class student:
    Institute_name="university of dayton"
    

def changeInsname(cls, name):
    cls.Institute_name=name
    print(f"the name of the institute is change to {cls.Institute_name}")

obj1=student
obj1.changeInsname=MethodType(changeInsname,student) # It is similar to adding bound methods with instance name(object_name)
# but here we are passing the class name along with the method defined outside the class....
obj1.changeInsname("Texas a&m")

