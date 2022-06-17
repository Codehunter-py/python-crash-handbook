import win32com.client as client

messageTo = ""
messageCC = ""
messageSubject = "" 
messageBody = ""
message = ""

while True:
    print("==== Press 'q' to quit ====")
        
    message = input("\nWho do you want to send a message? \n1) CSC 2nd Level \n2) CSC Operation \n3) ADD HERE \nChoose correct address or enter email address: ")
    if message == 'q':
        break
    elif message == "1":
        message += "CSC 2nd Level"
    elif message == "2":
        message += "CSC Operation"    
    else:
        messageTo = message + ""

    message = input("\nWho do you want to CC the message? \n1) CSC 2nd Level \n2) CSC Operation \n3) ADD HERE \nChoose correct address or enter email address: ")
    if message == 'q':
        break
    elif message == "1":
        message += "CSC 2nd Level"
    elif message == "2":
        message += "CSC Operation"  
    else:
        messageCC = message + ""

    message = input("\nSubject: \n1) CSC Deployment \n2) Patching servers \n3) ADD HERE \nChoose correct subject or add here: ")
    if message == 'q':
        break
    elif message == "1":
        message += "CSC Deployment"
    elif message == "2":
        message += "Patching servers"  
    else:
        messageSubject = message + ""

    message = input("\nAdd the body of the email: ")
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
    message.Body = messageBody
except AttributeError:
    pass

prompt= ""
while True:
    
    prompt = input("Do want to send the email? y/n ")
    if prompt == 'y':
        message.Send()
    else:
        break

    prompt = input("Do want to save the email? y/n ")
    if prompt == 'y':
        message.Save()
    else:
        break
