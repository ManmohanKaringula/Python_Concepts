class first():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def details(self):
        type="student"
        

# syntax to inherit __init__() method, use the below syntax if you want additional functionality to parent's class __init__
# method 
class second(first):
    def __init__(self, fname, lname):
        first.__init__(self, fname, lname)
        self.age=30
    def view(self):
        print(f'{self.fname} {self.lname} {self.age}') 
    
class third(first):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # using super() 
        self.age=22
    def view(self):
        print(f'{self.fname} {self.lname} {self.age}')   


obj1=second("manmohan", "reddy")
obj1.view()
obj2=third("yashwanth", "mudhiraj")
print(obj1.fname)
obj2.view()





