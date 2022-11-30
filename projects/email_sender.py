import smtplib

# ! receiveing sender email and password 

sender_email = 'pyaireza7@gmail.com'
receiver_email = 'ahashemi5665@gmail.com'
password = 'sdlrjodkrmawxgdc'
password = str(password)
message = "hey here we have something"

# todo connect to smtp server and login to our email account

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email,receiver_email,message)
print("Email has been sent to",receiver_email)





