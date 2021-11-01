########################################################
# This is for practicing and memorizing of code blocks #
#   Inspired by Python Crash Course Book 2nd Edition   #
########################################################

# prompt =("\nI am a bot!")
# prompt += ("\nI will repeat what you ask: ")
# message = ""
# active = True
# while active :
  #  message=input(prompt)
    
   # if message == 'quit':
    #    active = False
    #else:
     #   print(message)

#prompt = "\nPlease enter a city you have visited: "
#hile True:
    #city = input(prompt)

    #if city == 'quit':
        #break
    #else:
        #print(f"I would love to go to {city}")

#current = 0
#while current < 15:
 #   current += 1
  #  if current % 2 == 0:
   #     continue
#
 #   print(current) 

#x = 1
#while x <=6:
 #   print(x)
  #  x += 2

### 7-4 page 123
#prompt = "\nPlease add toppings: "
#prompt += """\nFor closing page please write 'quit'"""
#toppings = ""
#active = True
#while active:
 #   toppings = input(prompt)
    
  #  if toppings == "quit":
   #     break
    #else:
     #   print(f"{toppings} will be added to the pizza.")
#print("Process are completed")

### 7-5 movie tickets
#age = input("What is your age? ")
#age = int(age)
#active = True
#while active:
 #   if age <3:
  #      print("Ticket is free")
   #     active = False
    #elif age > 3 and age < 12:
     #   print("Ticket is 10$")
      #  active = False
   # else:
    #    print("Ticket is 15$")
     #   active = False

### 7-8 sandwich-orders
#sandwich_orders = ['pastrami', "Cheeseburger", 'pastrami', "Hotdog", 'pastrami', "Double Cheeseburger", "Spicy Wrap"]
#finished_sandwiches = []

#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')
#print("run out of pastrami")    

#while sandwich_orders:
 #   made_sandwiche = sandwich_orders.pop()
  #  print(f"I made your {made_sandwiche}")
   # finished_sandwiches.append(made_sandwiche)
#print("\nFinished sandwices: ")
#for finished_sandwich in finished_sandwiches:
 #   print(finished_sandwich)

### 7-10 Dream Vacation
#prompt = """If you could visit one place in the world, where
#would you go? """
#responses = {}
#poll_active = True

#while poll_active:
 #   name = input("Enter your name: ")
  #  place = input(prompt)
   # responses[name] = place
   # quit = input("Would you like to let another person respond? (yes/ no) ")
   # if quit == "no":
    #    poll_active = False

#for name, response in responses.items():
 #   print(f"{name} wants to be in {response}.")

### 8-3 T-Shirt

# def make_shirt(message, size='M'):
 #   print(f"{size} is size of your T-shirt with message: {message}")

#make_shirt('I love programming')

#def describe_city(city, country='Poland'):
 #   print(f"{city} is in {country}.")

#describe_city('Lublin')
#describe_city('Warsaw')
#describe_city('Poznan')

### 8-7 Album
#def make_album(artist, title, number_songs=None):
    
 #   album = {'Artist name' : artist, 'Album tite' : title}
 #   if number_songs:
 #       album['Number of Songs'] = number_songs
 #   return album
#while True:
 #   print("\nPlease enter artist name")
  #  print('Please enter title')
   # print("(please enter number of songs) optional")
   # print("to quit enter 'q'")
   # artist = input("Artist: ")
   # if artist == 'q':
   #     break
    #title = input('Enter title: ')
   # if title == 'q':
    #    break
    #number = input('Enter number of songs: ')
   # if number == 'q':
    #    break

#artist_album = make_album(artist,title,number)
# print(f"hello this your album {artist_album}")

# 8-9, 8-11 messages

#def show_messages(texts, sent_texts):
 #   while texts:
  #      current_text = texts.pop()
  #      print(current_text)
   #     sent_texts.append(current_text)

#def show_result(sent_texts):
 #   print("\nYour results: ")
  #  for sent_text in sent_texts:
   #     print(sent_text)

#texts = ["Hi, Please call me late", "I am not available", "Call now"]
#sent_texts = []

#show_messages(texts[:], sent_texts) # preserve the list with [:]
#show_result(sent_texts)
#print(f"\n{texts}")

# 8-12 sandwiches
# def sandwiches(*orders):
#    print("\nYour ordered selected sandwiches: ")
#    for order in orders:
#        print(order)

# sandwiches('cheeseburger', 'double cheeseburger')
# sandwiches("Pastrami")

# 8-13 Build Profile

# def user_profile(firstname, lastname, **user_info):
#    user_info['firstname'] = firstname 
#    user_info['lastname'] = lastname 
#    return user_info

# user = user_profile('John', 'Wick', location='LA')
# print(user)

###
#import module 
#import pizza
#pizza.make_pizza(16, 'pepperoni')

# module_name.function_name()
# module_name import fucntion_name()
"""Here we give the function make_pizza() an alias, mp(), by importing
make_pizza as mp. The as keyword renames a function using the alias you
provide:"""
"""from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')"""

# from modul_name import function_name as fn
# from module_name import *

### Chapter 9
# Creating a class

# class Dog:
#     # a simple attempt to model a dog.

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Stimulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         print(f"{self.name} rolled over!") 

#     def bark(self):
#         print(f"{self.name} can bark to other people.")    

# my_Dog = Dog('Max', 6)
# print(f"My dog's name is {my_Dog.name}.")
# print(f"My dog is {my_Dog.age} years old.")
# my_Dog.sit()
# my_Dog.roll_over()

# other_dog = Dog('Lucy', 6)
# print(f"\nIts name is {other_dog.name}")
# print(f"She is {other_dog.age} years old.")
# other_dog.sit()
# other_dog.roll_over
# other_dog.bark()

# # 9-1 Restaurant

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} has {self.cuisine_type} type of dishes in menu.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open now")

# my_restaurant = Restaurant("Kebab King", "Turkish") 
"""instance representing this particular dog and 
sets the name and age attributes using the values we provided."""
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# # 9-2 Three Restaurants
# print("\n")
# telaviv = Restaurant("Tel-Avive", "Vegan")
# telaviv.describe_restaurant()
# telaviv.open_restaurant()

# 9-3 Users

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         print(f"User's full name is {self.first_name} {self.last_name}")   

#     def greet_user(self):
#         print(f"{self.first_name} {self.last_name} welcome to our web-page!")     

# new_user1 = User('Jethro', 'Jenkins')
# new_user1.describe_user()
# new_user1.greet_user()

# 9-4 Number Served

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} has {self.cuisine_type} type of dishes in menu.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open now")

#     def served(self):
#         print(f"Restaurant has served {self.number_served} customer(s)") 

#     def set_number_served(self, numbers):
#         self.number_served = numbers
#         print(f"You have served {self.number_served}")      

#     def increment_number_served(self, add):
#         self.number_served += add     

# class Bakhlava(Restaurant):
    
#     def __init__(self, restaurant_name, cuisine_type='Bakhlava'):
#         super().__init__(restaurant_name, cuisine_type)
#         self.type = []

#     def show_type(self):
#         print('n\We have following types:')
#         for type in self.type:
#             print( "- " + type.title())    

# my_restaurant = Restaurant("Kebab King", "Turkish") 
# my_restaurant.describe_restaurant()
# sweet = Bakhlava('Kebab King')
# sweet.type = ["Fistikli", "Cevizli"]
# sweet.show_type()

# 9-5 Login Attempt (on hold)

# class User():
#     """Represent a simple user profile."""

#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the user."""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0

#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)

#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print("\nWelcome back, " + self.username + "!")

#     def increment_login_attempts(self):
#         """Increment the value of login_attempts."""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """Reset login_attempts to 0."""
#         self.login_attempts = 0

# eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
# eric.greet_user()

# print("\nMaking 3 login attempts...")
# eric.increment_login_attempts()
# eric.increment_login_attempts()
# eric.increment_login_attempts()
# print("  Login attempts: " + str(eric.login_attempts))

# print("Resetting login attempts...")
# eric.reset_login_attempts()
# print("  Login attempts: " + str(eric.login_attempts))

# from electric_car import Car

# my_old_car = Car('Skoda', 'Fabia', 2006)
# print(my_old_car.get_descriptive_name())

# from import_restaurant import Restaurant

# my_new_restaurant = Restaurant("Absheron", "Azeri")
# my_new_restaurant.describe_restaurant()
# my_new_restaurant.open_restaurant()

