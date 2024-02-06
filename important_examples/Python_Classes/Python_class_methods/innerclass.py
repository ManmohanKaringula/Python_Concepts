# The inner classes are not very useful but we can have inner classes in two ways
# 1. multiple inner classes
# 2. multilevel inner classes

# First  section: Here  we will see the multiple inner classes
class Doctors:
    def __init__(self):
        self.dn=self.Dentist()
        self.ca=self.Cardiologist()
    
    class Dentist:
        def __init__(self):
            self.name="avanthika"
            self.experience=40
        def showdetails(self):
            print(f"The dentist name is {self.name} and experience is {self.experience}")

    class Cardiologist:
        def __init__(self):
            self.name="ashok"
            self.experience=40
        def showdetails(self):
            print(f"The dentist name is {self.name} and experience is {self.experience}")

obj1=Doctors()
d=obj1.dn
d.showdetails()

#Second Section: Here we will see the multilevel inner classes

class superclass:
    def __init__(self):
        self.innerclass=self.innerclass()

    class innerclass:
        def __init__(self):
            self.leafclass=self.leafclass()
        class leafclass:
            def showdetails():
                print("This is the last class in the multilevel class hierarchy that is the leaf class")


obj1=superclass
godown1=obj1.innerclass
godown2=godown1.leafclass
godown2.showdetails()