# This is a simple SMTP client, made to send simple emails with python

# Import everything worth importing 
from socket import *
import sys

print "-------------------------------"
print "Welcome to a Simple Mail sending client!"
print "-------------------------------"

s = socket(AF_INET, SOCK_STREAM)

# Get SMTP server info
s.connect((raw_input("Enter SMTP server IP: "), 25))
if s.recv(100)[:3] != '220':
    sys.exit("Invalid SMTP server IP!")

# Get hostname
s.sendall("EHLO " + raw_input("Enter hostname: ") + '\n')
if s.recv(100)[:3] != '250':
    sys.exit("Invalid hostname!")
# LOGIN to server
s.sendall("AUTH LOGIN\n")
if s.recv(100)[:3] != '334':
    sys.exit("Can't login to server!")

# Get username and password
s.sendall(raw_input("Enter username: ") + '\n')
if s.recv(100)[:3] != '334':
    sys.exit("Invalid username!")

s.sendall(raw_input("Enter password: ") + '\n')
if s.recv(100)[:3] != '235':
    sys.exit("Invalid password!")

# Get the sender's email
s.sendall("MAIL FROM: <" + raw_input("Who is the mail from: ") + ">" + '\n')
if s.recv(100)[:3] != '250':
    sys.exit("Incorrect source email!")

# Get the recipient's email
s.sendall("RCPT TO: <" + raw_input("Who is the mail for:")+ ">" + '\n')
if s.recv(100)[:3] != '250':
    sys.exit("Incorrect destination email!")

# Last check before getting the msg
s.sendall("DATA\n")
if s.recv(100)[:3] != '354':
    sys.exit("The server does not want to send this mail")

# Getting the message from the sender
msg = raw_input("Write down your message(inorder to send, have a standalone line '.'):\n")
# While there isnt a standalone line with a value of '.', keep reading info into "msg"
while msg != '.':
    s.sendall(msg+'\n')
    msg = raw_input("")

# Send email finally and check that it has been delieverd
s.sendall(".\n")
if s.recv(100)[:3] != '250':
    sys.exit("Coudln't send your email, server dosent want to accept it")

# Quit the program, kill the connection and say a nice goodbye to the user
s.sendall("QUIT\n")
s.shutdown(SHUT_RDWR)
s.close()

print "Thank you for using the Simple Mail service!"

#FIN
