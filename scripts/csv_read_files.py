import pandas as pd
import os

files = os.listdir('c:\\Users\\W116267\\Downloads')
for file in files:
    print(file)

os.chdir('c:\\Users\\W116267\\Downloads')
filename = input("Enter csv filename: ")
text=''

while True:
    df = pd.read_csv (filename, index_col = 0, encoding="ISO-8859-1")
    print(df)
    text = input("Press 'q' to quit: ")

    if text == 'q':
        break

    