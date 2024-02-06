# We can unpack the sequences for the positional arguments of a function call 

# using list to upack for the arbitrary varibles 
def squaring(*args):
    for i in args:
        print(i*i)

a=[1,2,3,4,5] # The same goes with the tuple
squaring(*a)

# Using the dictionary for upacking the keyword arguments....
def show_users(**kwargs):
    for i in kwargs:
        print(f"The user name is {i} and his contact number is {kwargs[i]}")

x={"manmohan": "9177285721", "ajay": "8032829465"}

show_users(**x)

