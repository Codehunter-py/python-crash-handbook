# def replace_ending(sentence, old, new):
#     # Check if the old string is at the end of the sentence
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the 
#         # end with the new string
#         i = len(old)
#         new_sentence = sentence[:-i]+new
#         return new_sentence
#     # Return the original sentence if there is no match
#     return sentence


# ending = replace_ending("file.csv", "csv", "xlsx")
# print(ending)


# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = ""
#     reverse_string = ""
#     # Traverse through each letter of the input string
#     for letter in input_string.strip():
#         # Add any non-blank letters to the 
#         # end of one string, and to the front
#         # of the other string. 
#         new_string = new_string+letter.replace(" ","")
#         reverse_string = letter.replace(" ","")+reverse_string
#     # Compare the strings
#     if new_string.lower() == reverse_string.lower():
#         return True
#     return False
    
# print(is_palindrome("level"))

""" Static and Class methods"""
# class Person(object):
#     population = 50
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod # has access any variable defined inside class
#     def getPopulation(cls):
#         return cls.population    
#     @staticmethod # only has access to the argument
#     def isAdult(age):
#         return age >= 18

#     def display(self):
#         print(self.name, 'is', self.age, 'years old')

# newPerson = Person('ibo', 24)
# print(Person.isAdult(21))

# lis = [2, 4, 6]

# def func(x):
#     return x**2

# print(list(map(func, lis)))

# takes list and passes it to the list

""" Filter function """

# def add7(x):
#     return x + 7 

# def isOdd(x):
#     return x%2==0

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = list(filter(isOdd, a)) # output [2, 4, 6, 8]
# c = list(map(add7, b))  # ouput [9, 11, 13, 15]
# print(a)
# print(b)
# print(c)

"""Lambda"""

# def func(x):
#     return x + 5 

# func2 = lambda x: x+5
# print(func2(5))

# func3 = lambda x,y: x+y
# print(func3(4,5)) #output 9

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # output [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# newList= list(map(lambda x: x+5, a)) 
# print(newList)
# newList= list(filter(lambda x: x%2==0, a)) # output [2, 4, 6, 8, 10]
# print(newList)

""" Collections """

from collections import Counter
from hashlib import new
from itertools import count
from unicodedata import name

# c = Counter("gallad") # output Counter({'a': 2, 'l': 2, 'g': 1, 'd': 1})
# print(c)
# c = Counter(['a', 'a','b', 'c','c'])  # output Counter({'a': 2, 'c': 2, 'b': 1})
# print(c)
# c = Counter({'a' : 1, "b" : 2}) # output Counter({'b': 2, 'a': 1}) 
# print(c)
# c = Counter(cats=4, dogs=7) # output Counter({'dogs': 7, 'cats': 4}) 
# print(c)
# print(c.most_common(2)) # output [('dogs', 7), ('cats', 4)] 

"""#1 Interview question """

# names = ["Braylon", "Tim", "Ibo", "Tim", "Adele", "Sherlock", "Tim", "Ibo" ]
# newdict = {}
# for name in names: 
#     newdict[name] = names.count(name)
    
#     if name not in newdict:
#         newdict.append(name)

# print(dict(sorted(newdict.items(), key=lambda item: item[1], reverse=True)))

"""named tuple"""
# import collections
# from collections import namedtuple

# Point = namedtuple('Point', 'x y z')

# newP = Point(3, 4, 5)
# print(newP) # output Point(x=3, y=4, z=5)
# print(newP.x, newP.y, newP.z) # 3 4 5

# print(newP._replace(y=6)) # output Point(x=3, y=6, z=5)

"""CS50P - Lecture 7"""

# import re 

# email = input("Enter email: ").strip()

# if re.search("^\w+@(\w+\.)?\w+\.[a-zA-Z]{2,3}$", email, re.IGNORECASE):
#     print("Valid email")
# else:
#     print("Invalid email")

"""CS50P - Lecture 8"""

import random 

class Hat:
    houses = ["Gryffindor", "Huffkepuf", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls,name):
        for _ in range(5):
            print(name, "is in", random.choice(cls.houses))

# using name of class and accessing that class's objects
Hat.sort("Harry")