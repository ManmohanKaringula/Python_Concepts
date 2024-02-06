def sqr(x):
    return x*x

f=sqr # referencing a python function to variable, so the variable f acts as function 
print(f(5))
del sqr
print(f(6)) 