# defining a instance method is quite tricky if we don't want to use the constructor method("__init__")
# example to declare a instance method in a class without defining a constructor method explicitly
class testingClass:
    def getEmail(self, email): # we consider this a instance method (we can use whatever instead of self)
        self.email=email  # This is the main syntax that makes a method an instance method not the "self" keyword

firstperson=testingClass
# firstperson.getEmail("manmohanreddyk.999@gmail.com") // Error missing 1 required positional argument
# Important Note: The problem with instance method when declared without constructor (__init__) function in a class
#  is that we have to send the fist parameter as the object explicitly only then there will be no error

firstperson.getEmail(firstperson, "manmohanreddyk.999@gmail.com") # Now that we have send the object as the first parameter
# We get no error, again there is no such rule to send the object as first parameter if we are sending the object as the 
# parameter explicitly...

print(firstperson.email)

# The above mentioned method is very inefficient since the python interpreter can take care of sending "Object" as the parameter 
# but this time the interpreter will only send the Object as the first parameter hence we recongnize that with a standard word
# know  as "self"

# Example for the creation of the instance method using the constructor function (__init__)  in the class
class testingInstance:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getEmail(self, email):
        self.email=email

secondperson=testingInstance("Haritha", 25)
secondperson.getEmail("haritha@gmail.com")
print(secondperson.email)

# Note : It is always advisable to create a constructor fucntion in a class, so we can create a instance variable and 
# also skip the burden of sending the object as first parameter which will be handled by the interpreter itself.....



