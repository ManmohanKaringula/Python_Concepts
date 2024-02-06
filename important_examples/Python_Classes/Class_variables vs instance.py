
class Dog():

    attributes=[]  # declaring a list which is a class variable

    def __init__(self, name):
        self.breedname=name

    def traits(self, t1):
        self.tr=t1
        self.attributes.append(self.tr)
        

a=Dog("german shepard")
a.traits("running")
b=Dog("Dalmation")
b.traits("jumping")
c=Dog("rottweiler")
c.traits("biting")
print(c.attributes)

# you see in the above code making attributes list variable as class variable in Dog class makes the class faulty
# but it has its own benifits

class DOG():

    def __init__(self, name):
        self.breedname=name 
        self.attributes=[] # instance variable which is list

    def traits(self, t1):
        self.attributes.append(t1)
        print(f"The Dog name is {self.breedname} and it attribute is {self.attributes[0]}")

a=DOG("german shepard")
a.traits("running")
b=DOG("Dalmation")
b.traits("jumping")
c=DOG("rottweiler")
c.traits("biting")

# In the above code the attributes list variable which is an instance variable of a class which suits the purpose
# quite well and saperates the traits for different instances.....