# The class methods are used to modify the state and variables of a class 
# The class methods are declared with @classmethod

# Example
class student:

    course="Computer Science Engineering"

    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod # decorator that makes the function changeCourse have the first parameter as the classname, here we follow 
# the convention of having "cls" as the first parameter just like "self" for the instance methods
    def changeCourse(cls, coursename):
        cls.course=coursename 
    @classmethod
    def knowYourCourse(cls):
        print(f"your course name is {cls.course}")


obj1=student("Manmohan", 122)
print(obj1.name)
obj1.changeCourse("Electronics")
print(obj1.knowYourCourse())
