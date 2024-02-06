# We can pass the parameters in three ways positional-only, positional or keyword, keyword-only

# 1. to pass the arguments either by positional or keyword dont use any "*" or "/"
# 2. to pass the arguments positional-only use "/" after the parameters. 
# 2. to pass the arguments keyword-only use "*" before the parameters.

def standard_arg(arg):
        print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
     print(arg)

standard_arg(arg=23) # using the keyword argument
standard_arg(23) # using the positional argument

pos_only_arg(1) # this function only takes positional argument since it has "/" in its definition...

kwd_only_arg(arg=54) # this function only takes kekyword arguments since it has "*" in its defintion....
# kwd_only_arg(54), this would raise an error since it is restricted to only keyword argument....


