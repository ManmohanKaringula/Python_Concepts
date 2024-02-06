
""" The Generators are used to return the iterators, they can be implemented by using "yield" keyword """

import random

def create_emoticon_generator():
    while True:
        strings = "!@#$^*_-=+?/,.:;~"
        grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]
        grp = random.choice(grouped_strings)
        face_strings_list = [random.choice(strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        yield emoticon

# Because Generators return an Iterator there is no need for overriding the next() method of a iterator.
# There is no nedd to write the __next__() function in the create_emotion_generator() funciton while using "Yield" keyword.

