def func1(name,  **kwargs):
    return 'name' in kwargs

# func1(1, **{'name':'manmohan'})
# to resolve the above name collision 

def func2(name, /, **kwargs):
    return 'name' in kwargs

print(func2(1, **{'name':'Manmohan'}))