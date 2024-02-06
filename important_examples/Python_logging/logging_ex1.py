import logging # default level for logging is set to WARNING

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

logging.basicConfig(filename="E:\\Manmohan Files\\logfolder\\firstlog.log", level=logging.DEBUG, 
                     format='%(asctime)s:%(levelname)s:%(message)s') # Debug is a constant

num1=10
num2=5
result1=add(num1, num2)
logging.debug(f"The addition of {num1} and {num2} is: {result1}")

result2=subtract(num1, num2)
logging.debug(f"The subtraction of {num1} and {num2} is: {result2}")

result3=multiply(num1, num2)
logging.debug(f"The multiplication of {num1} and {num2} is: {result3}")

result4=divide(num1, num2)
logging.debug(f"The division of {num1} and {num2} is: {result4}") # debug is a method and the program works because the
# level is set to DEBUG constant "logging.basicConfig(level=logging.DEBUG)" in line 15.



