# The Locals() is a function which returns a dictionary which consists of local variable's name and value in key value pairs
# Example:

def something():
    x=3422
    print(locals())

something()       

class super1():
    def func1(self):
        y=3443
        print(locals()) 
        # The locals() function will return dictionary which consists of a self:address of self (because it is a reference variable), y and its value.

c=super1()
c.func1()

print(locals()["__file__"]) # this line is used to print the location of the file....