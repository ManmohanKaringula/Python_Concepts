class p1():
    def func1(self):
        print("This is the first function")

class p2():
    def func2(self):
        print("This is second function")

class p3(p1, p2):
    def func3(self):
        print("This is third function")


obj1=p3()
obj1.func1()
obj1.func2()
print(obj1.mro())
