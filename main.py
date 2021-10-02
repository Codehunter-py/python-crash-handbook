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

prompt = "\nPlease enter a city you have visited: "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city}")
   
