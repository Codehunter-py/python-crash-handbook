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

#8-12 sandwiches
#def sandwiches(*orders):
 #   print("\nYour ordered selected sandwiches: ")
  #  for order in orders:
   #     print(order)

#sandwiches('cheeseburger', 'double cheeseburger')
#sandwiches("Pastrami")

# 8-13 Build Profile

#def user_profile(firstname, lastname, **user_info):
 #   user_info['firstname'] = firstname 
  #  user_info['lastname'] = lastname 
   # return user_info

# user = user_profile('John', 'Wick', location='LA')
# print(user)

###
#import module 
import pizza
pizza.make_pizza(16, 'pepperoni')

