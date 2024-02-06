# Python decorators are functions/classes they are used to change the behaviour of a functions/classes decorator function/
# class are prefixed with @ before the function where you want to change the function/class functionality.

def super_function(original_function):

    def enclosed():
        print("This line is extension")
        return original_function()
    return enclosed # this is example of first class function.

@super_function  # This is similar is to func1()=super_function(func1) here the func1() is the closure.
def func1():
    print("Hii World")    

func1()

# Second_Part
def super_function1(original_function1):

    def enclosed():
        print("This line is another extension")
        return original_function1()
    return enclosed # this is example of first class function.

def func2():
    print("Hello World") 

func2=super_function1(func2)   
func2()
dd=super_function1(func2)
dd()