
class myclass:
    def x(): # it is method not a function
        pass
    print("Hello no error")

obj1=myclass
obj1.x() # this is similar to myclass.x(obj1) hence even though we din't sent a positional argument the interpreter
# didn't raise an exception this is because the function is in class if at all the function is present outside the class 
# then the interpreter would raise an exception
# Example:
#    def y(a):
#        print(a)

#    y() calling the function without position argument 
