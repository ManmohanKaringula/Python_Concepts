# We use self keyword for instance variable but we should have the method which uses self in a class, in our example we have 
# ss(self,a) in class abc 
class abc():
    def ss(self, a):
        self.a=a
        print(f"The number you have entered is {self.a}")

b=input("Enter the name: ")
cbz=abc()
cbz.ss(b)