import smtplib

content = 'content'
phrases = ["Hello %s, this is your old friend Jax the dog"%name, "This is %s, who is this?"]

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