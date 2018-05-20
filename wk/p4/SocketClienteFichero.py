import os, sys, socket

HOST = 'localhost'
PORT = 9869
ADDR = (HOST,PORT)
BUFSIZE = 4096
client = socket.socket()
client.connect(ADDR)
path = os.path.abspath("Fichero.txt")
print(path)
#bytes = open(videofile,'rb').read()
client.send(path.encode("utf-8"))
data = client.recv(1000)
#print(len(bytes))
print(data)
#client.send(bytes)

client.close()
