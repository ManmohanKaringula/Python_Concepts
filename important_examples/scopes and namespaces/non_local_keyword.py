# example of enclosing scope
def outer(): 
    var=22
    def inner():
        print("The value of var (using the enclosing scope): " + str(var))
    inner()
outer()

# example of enclosed scope
def outer1():
    var=33
    def inner1(): 
        var=16
        print("The value of var is (using the enclosed scope): "+ str(var))
    inner1()
outer1()

# using the non local keyword to change the values variabls local to outer function
def outer2():
    var=45
    def inner2():
        
        nonlocal var
        var =93
        print("The value of var is : "+ str(var))
    inner2()
    print(f"The value of the outer2's var is : {var}")

outer2()
    

