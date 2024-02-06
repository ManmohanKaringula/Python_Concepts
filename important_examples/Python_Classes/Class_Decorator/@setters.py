# The setters are used to set the values to parameters, for example if we give the fullname then it should change the 
# parameters firstname and lastname to do that we use setters in python using the "@<function_name>"

class employee:
    def __init__(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname

    @property
    def returnFullname(self):
        return f"{self.firstname}{self.lastname}"

    # The below code set the firstname and lastname once the fullname is passed...
    @returnFullname.setter
    def returnFullname(self, name):
        first, last =name.split(' ')
        self.firstname=first
        self.lastname=last

    # The below code is also a setter but it deletes the value in the firstname and lastname once the fullname is deleted..
    @returnFullname.deleter
    def returnFullname(self):
        print("The firstname and lastname are set to none")
        self.firstname=None
        self.lastname=None

emp1=employee("haritha", "Reddy")
print(emp1.returnFullname) # This is a getter method 
emp1.returnFullname="Manmohan Reddy"
print(emp1.firstname)
print(emp1.lastname)
print(emp1.returnFullname)
del emp1.returnfullname
print(emp1.firstname)
print(emp1.lastname)
print(emp1.returnFullname)






    