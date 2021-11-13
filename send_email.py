import win32com.client as client

messageTo = ""
messageCC = ""
messageSubject = "" 
messageBody = ""
message = ""

while True:
    print("==== Press 'q' to quit ====")
        
    message = input("\nWho do you want to send a message? ")
    if message == 'q':
        break
    else:
        messageTo = message + ""

    message = input("\nWho do you want to CC the message? ")
    if message == 'q':
        break
    else:
        messageCC = message + ""

    message = input("\nSubject: ")
    if message == 'q':
        break
    else:
        messageSubject = message + ""

    message = input("\nAdd the content of the message: ")
    if message == 'q':
        break
    else:
        messageBody = message + ""

    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()

try:
    message.To = messageTo
    message.CC = messageCC
    message.Subject = messageSubject
except AttributeError:
    pass

prompt= ""
while True:
    prompt = input("Do want to save the email? y/n ")
    if prompt == 'y':
        message.Body()
    else:
        break
    
    prompt = input("Do want to send the email? y/n ")
    if prompt == 'y':
        message.Send()
    else:
        break
        