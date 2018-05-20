import os, sys, socket

HOST = 'localhost'
PORT = 9848
ADDR = (HOST,PORT)
BUFSIZE = 4096
client = socket.socket()
client.bind(ADDR)
client.send(bytes("Dime la hora y la fecha","utf-8"))
data = client.recv(1000)
print(data)

client.close()
