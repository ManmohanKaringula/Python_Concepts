# The namedtuple is combination of both the dictionary and tuples, It is used to give the elements in the tuple a description 
# similar to the dictionary but the major difference comes when we wnat to have strictly immutable dictionaries

from collections import namedtuple 

#syntax: namedtuple(<name>,<items>)

student = namedtuple('student', ['name', 'age', 'DOB'])

s1=student('Akshith', 24, '09/08/1998')
s2=student('vineeth', 25, '07/08/1998')
s3=student('suresh', 25, '10/08/1998')

dict1={'name': "Vinod", "age": 23, 'DOB':"10/10/1998"}

# Methods of for accessing the namedtuple elements....
print(s1[1]) # This is the index based method of accessing the elements in the namedtuple
print(s1.name) # One of the advantages of using the namedtuple is that we can use the dot operator(".") 
print(getattr(s1,'DOB')) # We use the getattr method that takes the object name and its parameter

# Methods for conversion of the namedtuples

#_make() method is used to get namedtuple when an iterable is passed to the method
list1=['Raju', 21, '06/08/2000']
print(student._make(list1)) # we can store this in another variable if we want...

#_asdict() method is used to get an ordered dictionary 
print(s1._asdict()) # Output will be an ordered dictionary....

# **dictionary is used to convert the dictionary into a namedtuple
print(student(**dict1))

# Additional operators
#_fields() method is used to get all the feilds names that are used in the namedtuple 
print("The feilds that are used in the student namedtuple are: ")
print(s1._fields)

#_replace() method is used to change the values of a particulr attrubute
print(s1._replace(name="sanjay"))



