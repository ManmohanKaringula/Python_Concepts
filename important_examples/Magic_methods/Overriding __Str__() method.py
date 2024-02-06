class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

ee=Employee()
print(ee)  # The print keyword invokes __str__() method to print the strings but here we have overrided that method.
