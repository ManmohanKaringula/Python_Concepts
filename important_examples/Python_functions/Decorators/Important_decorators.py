"""In Decorators, functions are passed as an argument into another function
and then called inside the wrapper function."""

import functools

# Passing functions as parameters
def inc(x):
    return x+1
def dec(x):
    return x-1
def operator(func, a):
    temp=func(a)
    return temp
print(operator(inc, 12))
print(operator(dec, 11))

# passing parameters to the wrapper(inner) functions that are of another function which being decorated
def outer_div (func):
    @functools.wraps(func)
    def inner(x,y): # This is the wrapper function that is used to change the behaviour of the function that is passed.
        if (x < y): # Here x,y are the parameter of the passed function here they are parameter of divide function....
            x,y = y,x
        return func(x,y) 
    return inner

def divide (x,y):
     print (x / y)
divide1= outer_div(divide)
print(divide1(2,4))  # Here as you can see we have only created another function from passing the original function to the 
                     # decorator hence preserving the orginal function. This will not be the case with pie syntax....

# We will create another decorator that similar to the above one but using the pie syntax "@"

def outer_div2 (func):
    @functools.wraps(func)
    def inner(x,y): # This is the wrapper function that is used to change the behaviour of the function that is passed.
        if (x < y): # Here x,y are the parameter of the passed function here they are parameter of divide function....
            x,y = y,x
        return func(x,y) 
    return inner

@outer_div2
def divide2 (x,y):
     print (x / y)
divide2(2,4)

# Note: The only problem using the pie syntax is that it completely modifies whenevevr we use the function 

# Comprehensive examples on how to send parameters to the wrapper function inside the decorators...

def do_Double(func):
    def action():
        func()
        func()
    return action
def greet():
    print("Hello you are welcome")
greet=do_Double(greet)
greet()

# What happens if we send the below function to the do_Double decorator....
def greetInPerson(name):
    print(f"Hello {name} you are welcome")

try:
    greetInPerson1=do_Double(greetInPerson)
    greetInPerson1("Robert")
except Exception:
    print("This error is occuring because there are no arguments accepted by the wrapper function in the decorator \
           do_double function, we can solve this by adding the *args/**kwargs inside the wrapper function....")

# As we mentioned that we should add *args or **kwargs inside the wrapper function we create another decorator..
def do_Twice(func):
    def action(*args):
        func(args[0])
        func(args[0])
    return action
    
greetInPerson1=do_Twice(greetInPerson)
greetInPerson1("Robert") 

# we have to use either *args or **kwargs or parameters in the wrapper function of a decorator in order to send parametes 
# To the function that should be modified....




