
class instv():
    x=23  # It is a class variable and it is common to every class 
    def __init__(self, firstvar,secondvar):
        self.r=firstvar
        self.s=secondvar
        print(f"The values are {self.r}, {self.s}")

x=instv(565, 750)

print(f"The values of instance variables are: {x.r},{x.s}") 
# To access the instance variables the syntax is "object_name.variable_identifier" in the above case it is x.r, x.s .

print(x.x)

