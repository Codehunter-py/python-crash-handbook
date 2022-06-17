""" Chapet X """

import os
os.chdir('c:/Users/Ibrahim/Desktop/python-crash-handbook')

# filename = 'learning_python.txt'

# print("--- Reading in the entire file:")
# with open(filename) as f:
#     contents = f.read()
# print(contents)

# print("\n--- Looping over the lines:")
# with open(filename) as f:
#     for line in f:
#         print(line.rstrip())

# print("\n--- Storing the lines in a list:")
# with open(filename) as f:
#     lines = f.readlines()

# for line in lines:
#     line = line.rstrip()
#     print(line.replace('python', 'C'))

# print("=== Press 'q' to quit ===")
# file = "programming.txt"
# active=True
# text=''
# while active:
#     text=input("Note goes here: ")
#     with open(file, 'a') as file_object: #append and 'w' write
#         file_object.write(f"\n{text}")

#     if text == 'q':
#         active = False

"""Try and Except blocks"""

# filename = 'programming.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
# else:
#     # Count number of words in the file
#     words=contents.split()
#     num_words=len(words)
#     print(f"The file {filename} has about {num_words} words.")    

"""Working with multiple files"""

# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass #print(f"\nSorry, the file {filename} does not exist.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"\nThe file {filename} has about {num_words} words.")

# filenames = ['apache.txt' , 'programming.txt', 'python.txt']
# for filename in filenames:
#     count_words(filename)

# 10-6 Addition

# print("Enter 'q' at any time to quit.\n")

# while True:
#     try:
#         x = input("\nGive me a number: ")
#         if x == 'q':
#             break

#         x = int(x)

#         y = input("Give me another number: ")
#         if y == 'q':
#             break

#         y = int(y)

#     except ValueError:
#         print("Sorry, I really needed a number.")

#     else:
#         sum = x + y
#         print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

# 10-10 Common words

# filename = 'learning_python.txt'

# print("--- Reading in the entire file:")
# with open(filename) as f:
#     contents = f.read()
#     contents = contents.lower().count('python')
# print(contents)

"""Storing Data"""

# import json 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# filename = 'number.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

# # read the list back into memory
# with open(filename) as f:
#     numbers = json.load(f)

# print(numbers)

'''Saving & Reading User Generated Data'''
import json 

# username = input("What is your user name? ")
# filename = 'username.json'
# with open(filename, 'w') as f: 
#     json.dump(username, f)
#     print(f"{username} is added to json file!")

# with open(filename) as f:
#     username = json.load(f)
#     print(f"{username} is extracted from the json file")


### 10-11 Favorite number

# def get_stored_number():
#     filename = 'fav_number.json'
#     try:
#         with open(filename) as f:
#             number = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return number

# def store_fav_num():
#     number = input("What is your favorite number? ")
#     filename = 'fav_number.json'
#     with open(filename, 'w') as f:
#         json.dump(number, f)
#         return number

# def ask_fav_num():
#     number = get_stored_number()
#     if number:
#         print(f"I know your favorite number! It is {number}")
#     else:
#         number = store_fav_num()
#         print("Your favorite number is stored")        

# ask_fav_num()

"""Chapter XI"""
"""Testing code"""
# from name_function import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break

# formatted_name = get_formatted_name(first, last)
# print(f"\tNeatly formatted name: {formatted_name}.")

# import unittest
# from name_function import get_formatted_name
# class NamesTestCase(unittest.TestCase):

#     def test_first_last_name(self):
#         """Are all names string?"""
#         formatted_name = get_formatted_name('ibrahim', 'musayev')
#         self.assertAlmostEqual(formatted_name, 'Ibrahim Musayev')

# if __name__ == 'main':
#     unittest.main()

"""Automate Outlook email"""
#import win32com.client as client

# outlook = client.Dispatch("Outlook.Application")
# message = outlook.CreateItem(0)
# message.Display()
# message.To = ""
# message.CC = ""
# message.Subject = ""
# message.Body = ""
# message.Save()
# message.Send()