from multipledispatch import dispatch

#passing one parameter
@dispatch(int, int)
def product(first, second):
    result=first+second
    print(result)

#passing three parameters
@dispatch(int, int, int)  
def product(first, second, third):
    result=first+second+third
    print(result)

product(23,546,65)
product(34,546)
product(234, 342,44234)      
