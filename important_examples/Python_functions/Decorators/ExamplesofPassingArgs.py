"""def data_manipulation(modifying_function):
    def wrapper():
        modifying_function()  # remember that we are using the square() function and we are sending 5 as the parameter 
                                but we are not using any parameter here hence we can us the following syntax....
        print("The above function results in the square of the number")
    return wrapper """

def data_manipulation(modifying_function):
    def wrapper(*args, **kwargs):
        modifying_function(*args, **kwargs)
        print("The above function results in the square of the number")
    return wrapper
    
@data_manipulation 
def square(x):
    print(x*x)

square(5)