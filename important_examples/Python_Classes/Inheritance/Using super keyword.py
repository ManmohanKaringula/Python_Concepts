class first():
    type='student'
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname

class second(first):
    def __init__(self, age):
        self.age=age

class third(second):
    def __init__(self, fname, ):
        super().__init__(fname,)

obj1= first('manmohan', 'reddy')
obj2=second(30)
print(obj1.fname)

print(obj1.lname)


obj3=third('yashwanth',)
