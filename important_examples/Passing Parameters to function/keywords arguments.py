def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('--This parrot wouldn\'t', action, end=' ')
    print('if you put', voltage, 'volts through it' )
    print('-- Lovely Plumage, the', type)
    print("It's state", state, '!')

parrot(1000, 'hallow', )

# The following function calls will be invalid 
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# Note: At any cost passing positional arguments after key word argument will not work ....
