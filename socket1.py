import smtplib
import socket

serversmtp = smtplib.SMTP("smtp.gmail.com",476);
serversmtp.ehlo()
serversmtp.start()
host = char(input("enter server ip address : "))
port = int(input("enter port of server : "))
socket1 = socket.connect(host,port)
