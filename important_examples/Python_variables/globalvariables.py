# Scope: The scope of a variable decides where the variable can be accessed with in the program 
# Example: global variable can be used any where with in the program, whereas the local variable is used with in the 
# block of a code and not outside the block.

# Program:
a=10 # This is a global variable which can be accessed anywhere in the program.

def somemethod():
    a=12 # this is a local variable that can be accessed only with in this function.
    print(a) # local variable is printed.

somemethod() # calling the method.

print(a) # The global variable is printed.

b=15

def somemethod1():
    global b # using global keyword to change the value of b(global) inside the function
    b=17
    print(b)

somemethod1()
print(b)    # The changed value of b in somemethod1() function is printed  

c=87

def somemethod2():
    c=45
    globals()['c']=1 # The value of c is changed in the method but the local variable "c" is not changed but global "c"
                     # is changed that is because of the "globals()['c']" method, it returns the address of any global variable
    print(c)
    
somemethod2()
print(c)


