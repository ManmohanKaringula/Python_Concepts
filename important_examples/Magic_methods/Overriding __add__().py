"""
Method Overriding using __add__ method in python whenever "+" symbol is used operation is performed on based on the 
class of the object for integers addition is done where as for string concatination is done and here I have overrided the 
"+" Operator 
 """


class ss:
    def __init__(self, number):
        self.number=number

    def __add__(self,a):
        return self.number+a

dd=ss(6)
ans=dd+12
print(ans)
ans1= dd.__add__(113)  # hence this is similar to dd+113 ie., using "+" is similar to dd.__add__(113)
print(ans1)


