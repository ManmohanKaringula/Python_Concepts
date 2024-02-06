# The static methods in class has nothing to do with class variables and instance variables they are just like 
# regular functions that exists out if the class

class student:
    # The below mentioned method is a static method that cannot change the state of a class or object 
    def oddOrEven(x):
        if x%2==0:
            print("The given number is even number")
        else:
            print("The given number is not an even number")


person1=student
print(person1.oddOrEven(3))
