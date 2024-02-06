# The UserDict is a class from the collections module that is used to change the functionality of the original dictionary 
# The UserDict acts as the wrapper on the original library we can also override the magic methods of the dictionary

from collections import UserDict

class mydictionary(UserDict): # Using the UserDict class for inheritance and override/ create new methods
    def letsprintvalues(self):
        for i in self.values():
            print(i)

person=mydictionary({"name":"manmohan", "age": 23})
print(person.letsprintvalues())

# As you can we the UserDict lets us define our own methods for the dictionary and we can also change the original magic 
# Methods as well....
# similar to the UserDict we also have UserString and UserList in python which acts as wrapper to python strings and lists....


