# Every function in python is a first class function which means it has the privilage to act and operate on anyway
# here below the function take many forms like variables as well as arguemnts another function
import sys
def square(x):
    return x*x
q=square(5)
# In the above statement we are assigning the function to a variable
print(q)
f=square
# In the above statement we are treating square function as variable hence () are not mentioned
print(f)
print(square)
print(f(6))
# f is the variable to which square function is assigned as a variable and f may be a variable but can also act as a function(f(6))

def squarereturn(func, arglst):
    result=[]
    for i in arglst:
        result.append(func(i))
    return result

s=squarereturn(square, [1,2,3,4,5]) # sending square function as argument and a list

print(s)
# In the above function squarereturn accepts function and a list as arguments


def log(msg):

    def inner_log():
        print(f"The message is {msg}")

    return inner_log # returning function as a variable hence we shouldn't mention () notation.

hh=log("Hello my name is manmohan reddy karingula") # the log function return a function (inner_log()) 

hh() # this is what clousre is where hh() function is called and the value of msg is remembered 

#output: "Hello my name is manmohan"

# In the above program a function is retured or we can say that hh is same as inner_log()
# the inner_log() is the enclosed function while log() is the enclosing function, the enclosed function can use all the variables
# of an enclosing function freely:-)  

def log(msg):

    def inner_log():
        return msg

    return inner_log

hh=log("Hello my name is manmohan")

print(hh())
# the above code is similiar to the previous code but hh() function is callable, the inner_log() function returns the msg
print(sys.argv[0])

