# There could only be keywords after the arbitrary parameter that are passed to the function

def concat(*args, sep='/'):
    return sep.join(args)


print(concat("earth", "mars", "venus"))