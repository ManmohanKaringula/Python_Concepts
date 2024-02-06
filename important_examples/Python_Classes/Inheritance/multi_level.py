class parent():
    def func1():
        print("This is function one")

class C1(parent):
    def func2():
        print("This is function two")

class C2(C1):
    def func3():
        print("This is function three")

obj1=C2
obj1.func2()
obj1.func1()
obj1.func3()
print(obj1.mro())
