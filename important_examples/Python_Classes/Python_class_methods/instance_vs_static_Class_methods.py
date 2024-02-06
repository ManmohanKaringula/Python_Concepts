# Coming to the methods in python, the static method and class method are the not the same YES! they are totally different.
# There are two types of variables in python classes (static or class variables, non-static or instance variables)

# when you want to declare a method as instance method use "self" keyword in the paranthesis "(self, a,b,..)" of a method.
# When you want to declare a method as class method use "cls" keyword in the paranthesis "(cls,a,b,...)" of a method.
# and use @classmethod decorator.
# when you want to declare a method as static method dont use any paramaters in "()" and use @staticmethod decorator. 

class student():

    institute="Waste_of_TIME University" # Now this is static/class variable since it is declared outside the methods present 
                                         # in the class   

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3 # the class/static variable cannot be accessed by an instance method.
        
    def average(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_in(cls):
        print(f"This is a class variable, the name of the institute {cls.institute}")

    @staticmethod
    def info():
        print("This is a static method")

stu1=student(12,14,15)
print(stu1.average())
stu1.get_in()
stu1.info()






        