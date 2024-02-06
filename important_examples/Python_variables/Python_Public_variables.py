# By default every variable in class is a public variable
# The public variables in a class can be accessed anywhere in the module
class dpp():
    a=23   # By default this is a public variable
    
class spp(dpp):
    def meth1(self):
        print(f"this is public variable {self.a}")
obj1=dpp
print(obj1.a)

