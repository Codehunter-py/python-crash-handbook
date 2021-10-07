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

# 7-4 page 123
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

# 7-5 movie tickets
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

# 7-8 sandwich-orders
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

# 7-10 Dream Vacation
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
