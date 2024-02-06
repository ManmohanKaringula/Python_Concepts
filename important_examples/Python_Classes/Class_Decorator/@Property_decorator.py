# In programming languages like java there are methods called setters and getters which are used to modify the values and 
# get the values but in python language we use the @propery decorator....

# Example

class employee:
    def __init__(self, f,l):
        self.firstname=f
        self.lastname=l
        self.email=f"{self.firstname}{self.lastname}@email.com"

    def generatefullname(self):
        return f"{self.firstname} {self.lastname}"

emp=employee("Manmohan", "Reddy")
print(emp.generatefullname())
print(emp.email)
print("\n")
# The problem with the above class definition is that once the firstname or lastname in changed dynamically then the email wont get updated
emp.firstname="Rohit"
print(emp.generatefullname())
# But the problem is with email 
print(emp.email)  # output: ManmohanReddy@email.com even after changing the name there is no change in the email 
# To overcome the above situation where if we change one field there should be change in other fiels as well we generally use getters and setters methods 
# which happen to change the effected fields automatically but here in python we use a decorator called @property which changes the values instantly 
# when we call the function in a way we call the atrribute of a class....
print("\n")

# Example code:

class employee1:
    def __init__(self, f, l):
        self.firstname=f
        self.lastname=l

    def email(self):
        return f"{self.firstname}{self.lastname}@email.com"

    def fullname(self):
        return f"{self.firstname}{self.lastname}"

emp1=employee1("Rakesh", "kapoor")
print(emp1.fullname()) # RakeshKapoor
print(emp1.email())  # RakeshKapoor@email.com
print("\n")
emp1.firstname="Roshan" # Chaning the first name  
print(emp1.email()) # RoshanKapoor@email.com
print(emp1.fullname()) # RoshanKapoor
# From the above syntax and concept we are able to successfully change the  email field once firstname or lastname is changed 
# but the problem is we are calling the email as function with "()" not as an attribute, to solve this we can use the @property decorator which in turn
# calls all email function as class's attrubute

# Example code 3:
class employee3(employee1):
    @property
    def email(self):
        return f"{self.firstname}{self.lastname}@email.com"

emp3=employee3("Suresh", "Agarwal")
print(emp3.fullname())
print(emp3.email)   # We are calling the email() function as if it is an attribute .email this is only possible with @property decorator
print("\n")
emp3.firstname="yash" # changing the fistname in the emp3 object

print(emp3.fullname()) # we are calling fullname function as usual not like an attribute since it has no property decorator....
print(emp3.email)




