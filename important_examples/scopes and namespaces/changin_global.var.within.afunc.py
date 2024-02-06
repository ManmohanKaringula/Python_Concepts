x=12# this is global variable by default
print("The value of x before changing: "+str(x))

def test():
    global x #using the global keyword
    x=4345
    print("This the varible x which changes the value of x(global): "+ str(x))

test()
print("The value of the global variable x changes from 12 to 4345 by the function test() using global keyword: "+ str(x))