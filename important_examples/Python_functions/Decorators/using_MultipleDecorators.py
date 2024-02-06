def uppercase_decorator(function):
    def wrapper():
        func=function()
        return func.upper()
    return wrapper

def split_decorator(function):
    def wrapper():
        func=function()
        return func.split()
    return wrapper

@split_decorator
@uppercase_decorator
def say_hii():
    return "hello there"

print(say_hii()) # ["HELLO", "THERE"]
print(say_hii()) # ["HELLO","THERE"]
