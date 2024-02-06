""" The default value is evaluated only once. This makes a difference when the default is a mutable object 
such as a list, dictionary, or instances of most classes. For example, the following function accumulates the
 arguments passed to it on subsequent calls 
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print("\n")
""" 
    output:[1]
        >>>[1,2]
        >>>[1,2,3]
"""
""" To avoid this situation we can make use of None KEYWORD and for the L attribute and append the a new value 
everytime in the function is called only the new value will displayed.
"""

def f(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))