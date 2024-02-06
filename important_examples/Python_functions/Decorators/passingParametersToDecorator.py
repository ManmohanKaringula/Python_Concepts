# Apart from passing the parameters to the wrapper function inside the decorator we can also pass the parameters to the 
# decorator aswell 
import functools

def opener(num):
    def innerfunction(func):  # Even though innerfunction is the actual decorator the opener function is enclosing the decorator
                              # and providing the values to the decorator....
        @functools.wraps(func)
        def wrapper(*args):
            for i in range(num):
                func(args[0])
        return wrapper
    return innerfunction

@opener(3)  # here we are passing the arguments to the decorator.
def greetInPerson(name):
    print(f"Hello {name} you are welcome")
greetInPerson("Robert")

