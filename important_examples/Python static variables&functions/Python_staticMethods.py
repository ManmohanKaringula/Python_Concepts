# The static/class methods can be created staticmethod() or @staticmethod Decorator...

class super():
    def addition(self, a, b):
        self.a=a
        self.b=b
        return self.a+self.b

    def subtraction(self, a, b):
        self.a=a
        self.b=b
        return self.a+self.b

super.addtion=staticmethod(super.addition)
super.subtraction=staticmethod(super.subtraction)

addition(5,6)