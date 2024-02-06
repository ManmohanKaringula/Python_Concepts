"""The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, 
dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on 
subsequent calls"""
def func1(a, L=[]):
    L.append(a)
    print(L)

func1(1)
func1(2)
func1(3)

# To overcome this problem we use the following method

def func2(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    print(L)

func2(1)
func2(2)
func2(3)

# therefore passing the mutable objects as parameter accumulates the output of the instance of the fucntion.....




