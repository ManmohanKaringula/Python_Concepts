# Python sets are similar to other iterables like lists, dictionaries etc but there are some differences some of them are 
# a set cannot have duplicate elements and the operations that are performed on sets are the one that we perform on 
# mathematical sets (union, intersection, XOR, difference, symmetric difference etc..,), they are mainly used in database operations.
# Sets in python can grow and shrink in size like lists, they are iterable
# However sets are unordered and do not map keys to values, they are neither sequences nor mapping types

x=set('abcdefg')
y=set('abcdefghijlk')
print(x-y) # Difference
print(y-x) # Difference
print(x|y) # Set union
print(x&y) # Set Intersection
print(x^y) # Set Symmetric difference (XOR)
print(x>y, x<y) # Superset and subset
# In addition to expressions, the set objects provides methods that correspond to these operations and more
z=x.intersection(y) # This is similar to x|y;
print(z)
z.add("spam")
print(z)

