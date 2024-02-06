# Everything in python is an object, that is they are instances of one perticular class Ex: int, string are all classes...
a=12
print(a)
print(type(a))  #<class 'int'>

class super():
    pass

print(super()) # It will print the object (instance of super classs) at a random location 
# The class is also an object of a class know as "type" which is what we refer to metaclass 
# The metaclass type is the top most class in the python class hierarchy every other class like int, string etc are all the 
# instances of the "type" class....

print(type(int))
print(type(str))
# Since any userdefined or predefined classes are all the instance of the metaclass "type", we can create a class with
# Syntax other than using the keyword "Class"

#Syntax: type('name_of_the_class', (super_className for inheritance), {class properties})

def greet(self):
    self.message="Hello"
    print(self.message)

Test=type("Test", (), {"x":50, "greet":greet}) # this is similar to    class Test: x=50

a=Test
print(a.x)
print(a) # print which class does the object belongs to..          
a.greet(a)