import smtplib
print("Version 0.1")

print("Contacts do not reset when file is closed...")

contact_name = "n/a"
contact_email = "n/a"


name_ = open("name.txt", "w")
contacts = open("contacts.txt", "w")

def getContacts(name, email):
    contacts = open("contacts.txt", "w")
    contacts.write("\n" + email)
    contacts.close()
    name_ = open("name.txt", "w")
    name_.write("\n" + name)
    name_.close()

def useContacts(name):
    i = 1
    name_ = open("name.txt", "r")
    contacts = open("contacts.txt", "r")
    check = name_.readline(i)
    if check == name:
        target = email.readline(i)
        print(target)
    elif name_.readline(i) == "":
        print("Your contact does not exist!")
        pass
    else:
        i += 1

while contact_name != "" and contact_email != "":
    contact_name = input("Enter contact name here -> ")
    contact_email = input("Enter contact email here -> ")
    if contact_name != "" and contact_email != "":
        getContacts(contact_name, contact_email)
    else:
        print("Ok, I see you have no more contacts to add, lets continue with the scheduled program")

testContact_name = input("-> ")
useContacts(testContact_name)
content = 'content'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

""" Get the login information of the user """
user = input('Enter your gmail username (without @gmail.com) -> ')
pw = input('Enter the password that goes with this account -> ')
username = user + "@gmail.com"

""" Get the information attatched to the email """
text = input('What do you want the body of the email to say? -> ')
subject = input('What is the subject of the email? -> ')
msg = "Subject {}\n\n{}".format(subject, text)
contact_use = input("Do you want to use contacts? [1] = yes [2] = no -> ")
if contact_use == "1":
    print("(It is case-sensitive!)")
    chosen_name = input("What is the name of your contact?")
    useContacts(chosen_name)
if contact_use != "1":
    target = input('Who do you want to send the email to? -> ')

server.login(user, pw)
print('Login for %s successful'%username)

print('Confirm email send? [Y] or [N]')
ans = input('-> ')
if ans == "Y":
    server.send(username, target, msg)

while True:
    checkInfo = input("Do you want to change the info? [Y] or [N] -> ")
    if checkInfo == "Y":
        user = input('Enter your gmail username (without @gmail.com) -> ')
        pw = input('Enter the password that goes with this account -> ')
        username = user + "@gmail.com"
        text = input('What do you want the body of the email to say? -> ')
        subject = input('What is the subject of the email? -> ')
        msg = "Subject {}\n\n{}".format(subject, msg)
        contact_use = input("Do you want to use contacts? [1] = yes [2] = no -> ")
        if contact_use == "1":
            print("(It is case-sensitive!)")
            chosen_name = input("What is the name of your contact?")
            useContacts(chosen_name)
        if contact_use != "1":
            target = input('Who do you want to send the email to? -> ')
        server.ehlo()
        server.starttls()
        server.login(username, pw)
        print('Login for %s successful'%username)
        command = input("What shall it be boss? -> ")
        if command == "single":
            server.send(username, target, msg)
        if command == "spam":
            num = input("How many emails? (* means infinite) -> ")
            if num != "*":
                for x in range(0, int(num)):
                    server.send(user, target, msg)
            if num == "*":
                while True:
                    server.send(user, target, msg)
    """ It just continues along if the answer is not Y """
    command = input("What shall it be boss? -> ")
    if command == "single":
        server.ehlo()
        server.starttls()
        server.login(username, pw)
        server.send(username, target, msg)
    if command == "spam":
        num = input("How many emails? (* means infinite) -> ")
        if num != "*":
            for x in range(0, int(num)):
                server.ehlo()
                server.starttls()
                server.login(username, pw)
                server.send(username, target, msg)
        if num == "*":
            while True:    
                server.ehlo()
                server.starttls()
                server.login(username, pw)
                server.send(username, target, msg)
