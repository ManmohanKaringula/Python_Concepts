#we use map function to convert a list of values in a iterable by passing it into a common function 
# map syntax: map(function, iterable)
# Example:
num=[1,2,3,4,5,6,7]

def even(n):
    if n%2==0:
        return n

def addition(n):
    return n+n
# remember to use list() because the map() form mapping objects these objects are converted into list using 
# list() method.
x=list(map(addition, num))
print(x)

# Using map and lambda functions together
# Example:
y=list(map(lambda a:a+a, num))
print(y)
# In the above code we created a lambda function(anonymous function) for the addition() function hence the code
# is reduced in size.


# filter() function filters the values present in an iterable and stores the filtered 
# using filter function using lambda function
# Example:
z=list(filter(lambda b:b%2==0, num))
print(z)
z1=list(map(lambda b:b%2==0, num))
print(z1)
# above the map function will give the result as [false, true, false, true, false,....], the map function will give the
# output like that because it evalutes the expression according to the condition and produces the boolean value.
# map() funciton is better used when there should be a change to the values provided not while evaluating a condition for 
# the provided values in that case it is better of to use the filter() condition where the values are filtered according to 
# the condition provided.... 


# using filter() function with out lambda:
# Example:
p=list(filter(even, num))
print(p)



