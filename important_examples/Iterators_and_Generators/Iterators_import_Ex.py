# iterator_example.py
"""
This should give an iterator with a emoticon. The iterator is an object that returns the values in it when a method called 
next(iterator) or iterator.__next__() is called.
"""

import random

class CoolEmoticonGenerator(object):
    """docstring for CoolEmoticonGenerator."""

    strings = "!@#$^*_-=+?/,.:;~"
    grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]

    def create_emoticon(self, grp):
        """actual method that creates the emoticon"""
        face_strings_list = [random.choice(self.strings) for _ in range(3)]                     
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        return emoticon

    def __iter__(self):
        """returns the self object to be accessed by the for loop"""
        return self

    def __next__(self):  # As you can see the __next__() is overrided in here in the CoolEmoticonGenerator.
        """returns the next emoticon indefinitely"""
        grp = random.choice(self.grouped_strings)
        return self.create_emoticon(grp)
