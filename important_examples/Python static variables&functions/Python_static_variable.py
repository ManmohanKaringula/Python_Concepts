from unicodedata import name


class super():
    branch="cse"# this is a class or static variable
    def __init__(self, name, rollnum):
        self.name=name
        self.rollnum=rollnum

stu1=super('Manmohan', '16621A0580')
stu2=super('yashwanth', '16621A0562')

print(stu1.name)
print(stu1.branch)

print(stu2.name)
print(stu2.branch)  

# To change the static variable of an instance(Object) 
stu2.branch="mech"
print(stu2.branch)
print(stu1.branch) # output: cse

# To change the static variable of a whole class 
super.branch="ece"

print(stu1.name)
print(stu1.branch)
print(stu2.branch)