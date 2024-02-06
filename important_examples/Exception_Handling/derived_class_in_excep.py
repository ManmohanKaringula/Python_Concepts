class B(BaseException):
    print("hello")
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [D, C, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# output: D C B
# the output is B C D because the derived class ie 'C','D' cannot handle the parent class 'B' hence the except
# clause goes down one by one and reaches class "B" exception handler 
# CONCLUSION: any Child/Derived exception handler class cannot handle exception raised by the Parent/Base exception 
print("\n")
# Example 2:
class B(Exception):
    print("The order of the except clauses are reversed checkout the effect MANNNN!!!! ")
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
# In the above code the except classes are reversed, the outcome is that the Parent/Base exception handler will alone handle
# the Child/Derived class.Derived exception can be handled by the Parent exception handler

# Output: 
B
B
B
# this is because the "B" exception handler handles all other Child classes of it

# SAFE PRACTICE: it is best to have the derived/Child exception class in the except clause first and then after we should 
# declare except clause with parent/base clause.
 