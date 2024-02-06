import functools  
  
def count_function(func):  
    @functools.wraps(func)  
    def wrapper_count_calls(*args, **kwargs):  
        wrapper_count_calls.num_calls += 1  
  
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")  
        return func(*args, **kwargs)  
  
    wrapper_count_calls.num_calls = 0  
    return wrapper_count_calls  
  
@count_function  
def say_hello():  
    print("Say Hello")  
  
say_hello()  