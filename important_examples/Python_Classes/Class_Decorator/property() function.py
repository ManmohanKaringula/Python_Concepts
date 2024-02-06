# The property function is similar to the @property decorator 
# Example:

class employee:
    def __init__(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname


    def returnfullname(self):
        self.fullname=self.firstname+' '+self.lastname
        print(self.fullname)

    def updatefullname(self, name):
        first, last= name.split(' ')
        self.firstname=first
        self.lastname=last

    name=property(None, updatefullname)

emp1=employee("Haritha", "Reddy")
emp1.returnfullname()
emp1.name="Manmohan Reddy"
emp1.returnfullname()
    