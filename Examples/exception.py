# import module sys to get the type of exception
import sys
from fractions import Fraction
# Here, we print the name of the exception using the exc_info() function inside sys module. We can see that "a" causes ValueError and 0 causes ZeroDivisionError
# If for the first element 0 the exception is not handled the execution stops once zero is taken and if we handle execption using try and except block then the execution continues till the final element in the list.

randomList = [0,'a', 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", Fraction(r))
