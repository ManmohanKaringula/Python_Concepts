# Lambda_syntax: lambda argument1, argument2, argument3: expressions
# Lambda functions are used to create anonymous small functions
# syntax: lambda(keyword) arguments=one line expression

x=lambda y: y*y 
print(x (55))

# list comprehension is used to write concise methods
num=[1,2,3,4,5,6,7]
sum=[i for i in num]
print(sum)

# using List comprehensions and lambda functions together, we should have '(x)' after lambda expression
square=[(lambda x: x*x)(x) for x in num]
print(square)

# Using lambda function to check whether a value is grater than 5 or not:


check_num= lambda y:'the given value is greater than five' if y>5 else 'The given value is smaller than five'
print(check_num (12))

supper=list((map(x,num)))
print(supper)