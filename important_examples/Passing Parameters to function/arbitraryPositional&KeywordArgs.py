
# *args: this used to store many random positional arguments in a tuple named "args"
# **kwargs: this used to store many random keyword arguments in a dictionary named "kwargs"

# It is a standard that is followed by the python programmers to use "*args" and "**kwargs" but we can also use any identifier
#  instead of args and the kwargs just remember to use the "*" for arbitrary positional arguments and "**" for arbitrary 
# keywords arguments

#Examples:

def func2(*posi_arguments, **keyword_arguments):
    for i in posi_arguments:
        print(i)
    for j in keyword_arguments:
        print("The marks of subject", j, "is:", keyword_arguments[j] )

func2("manmohan", "someone1", "someone2", Maths=95, Science=87, English=90)