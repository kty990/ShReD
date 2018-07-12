import smtplib

content = 'content'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()

""" Get the login information of the user """
user = input('Enter your gmail username (without @gmail.com) -> ')
pw = input('Enter the password that goes with this account -> ')

""" Get the information attatched to the email """
text = input('What do you want the body of the email to say? -> ')
subject = input('What is the subject of the email? -> ')
msg = "Subject {}\n\n{}".format(subject, msg)
target = input('Who do you want to send the email to? -> ')

server.login(user, pw)
print('Login for %s successful'%user)

print('Confirm email send? [Y] or [N]')
ans = input('-> ')
if ans == "Y":
    server.send(user, target, msg)

while True:
    checkInfo = input("Do you want to change the info? [Y] or [N] -> ")
    if checkInfo == "Y":
        user = input('Enter your gmail username (without @gmail.com) -> ')
        pw = input('Enter the password that goes with this account -> ')
        text = input('What do you want the body of the email to say? -> ')
        subject = input('What is the subject of the email? -> ')
        msg = "Subject {}\n\n{}".format(subject, msg)
        target = input('Who do you want to send the email to? -> ')
        server.ehlo()
        server.starttls()
        server.login(user, pw)
        print('Login for %s successful'%user)
        command = input("What shall it be boss? -> ")
        if command == "single":
            server.send(user, target, msg)
        if command == "spam":
            num = input("How many emails? (* means infinite) -> ")
            if num != "*":
                for x in range(0, int(num)):
                    server.send(user, target, msg)
            if num == "*":
                while True:
                    server.send(user, target, msg)
    command = input("What shall it be boss? -> ")
    if command == "single":
        server.ehlo()
        server.starttls()
        server.login(user, pw)
        server.send(user, target, msg)
    if command == "spam":
        num = input("How many emails? (* means infinite) -> ")
        if num != "*":
            for x in range(0, int(num)):
                server.ehlo()
                server.starttls()
                server.login(user, pw)
                server.send(user, target, msg)
        if num == "*":
            server.ehlo()
            server.starttls()
            server.login(user, pw)
            while True:
                server.send(user, target, msg)
