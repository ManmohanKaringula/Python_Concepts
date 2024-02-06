# function defined outside the class and the function is similar to global variable, hence it is assigned to a class 
# variable inside (g=f)

def f(a):
    x=a
    print(x)

class thatclass():
    g=f
    g(5)
    f(5)

w=thatclass()