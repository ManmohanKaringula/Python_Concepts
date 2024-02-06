# In python we can override the class with the help of the metaclass keyword, usually it is metaclass=type but we can override
# it with userdefined class ...

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))