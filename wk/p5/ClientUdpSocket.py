import os, sys, socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
#el puerto tiene que ser distinto al del server
server_address=("127.0.0.1", 4001)
s.bind(server_address)
s.sendto(bytes("Dime la hora y el dia","utf8"),('127.0.0.1',4002))
datos=s.recv(1000)
print(datos)
