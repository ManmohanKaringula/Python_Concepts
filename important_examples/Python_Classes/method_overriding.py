# NOTE : below example is for method overriding and python doesn't support method overloading.

class parentlife():
    def Property(self):
        print("giving assets")

    def carrer(self):
        print("you have to study B.tech and become engineer")

class mylife(parentlife):
    def carrer(self):
        print("No i will become IPS at any cost")

obj1=parentlife()
obj2=mylife()

obj1.Property()
obj1.carrer()
obj2.Property()
obj2.carrer()

