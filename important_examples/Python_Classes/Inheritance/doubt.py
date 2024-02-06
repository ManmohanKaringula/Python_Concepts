class p1:
    def __init__(self):
        print("This is P1's constructor")

class p2:
    def __init__(self):
        print("This is p2's constructor")

class p3(p2, p1):
    pass  # Here the p2 constructor is inherited first since it is mentioned first in the parameter list
    
class p4(p2, p1):
    def __init__(self):
        p1.__init__(self)
        """ here irrespective of how the paramter list, the constructor is inherited which is mentioned inside
        the class's constructor"""

obj1=p3()                                 



