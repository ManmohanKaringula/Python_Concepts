# The itertools are used to manage and compute various results from iterabes like lists etc...,

from itertools import accumulate, combinations, combinations_with_replacement, permutations, product

a=[1,2,3]
b=[4,5]
print(list(product(a,b)))

# We can also use the permutations for a list 
#Ex:
print(list(permutations(a)))
print(list(permutations(a, 2)))

# Combinations
print(list(combinations(a,2)))
print(list(combinations_with_replacement(a,2)))
print(list(combinations_with_replacement(a,2)))
print("\n")
# We can also print the accumulated sum of an iterator
print(a) 
print(list(accumulate(a))) # it is similar to the fibonacci series


