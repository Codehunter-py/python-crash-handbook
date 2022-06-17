""" Chapet X """

import os
os.chdir('c:/Users/Ibrahim/Desktop/python-crash-handbook')

print("=== Press 'q' to quit ===")
print("=== Press 's' to display note ===\n")
file = "programming.txt"
active=True
text=''
while active:
    text=input("Your Note goes here: ")
    if text != 'q':
        with open(file, 'a') as file_object: #append and 'w' write
            file_object.write(f"\n{text}")
    else:
        active = False

    if text == 's':
        with open(file) as f:
            contents = f.read()
            print(contents)          
