# The creation of class dynamically is not used much but we can still use the type(class_name, superclass_name, attribute_list)

class A:
    pass
print(type(A))  #output: <class 'type'> 
print(A)
# As we can see here the type of class A is "type", therefore the any class is of type "type" and hence it is instance of 
# class type where metaclass is the sub class of the class type.....

# Creating a class instantly with type method...

A=type("super", (), {})
print(A)
print(type(A))

# I hope you got this....