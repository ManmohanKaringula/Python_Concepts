
class decclass:
    def __init__(self, func):
        self.func=func
    def __call__(self, *args, **kwargs):
        if args[1]==0:
            return "you can't divide"
        else:
            self.func(*args)

@decclass
def run(a,b):
    return a/b

print(type(run))
print(run(10,0))