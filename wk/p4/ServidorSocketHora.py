import socket, sys, socket, time

HOST = 'localhost'
PORT = 9849
ADDR = (HOST,PORT)
serv = socket.socket()

serv.bind(ADDR)
serv.listen(10)

print ('listening ...')

while True:
    serv, addr = serv.accept()
    print ('client connected ... ', addr)
    while True:
        data = serv.recv(10000)
        hora = time.strftime("%c")
        hora2=bytes(hora, "utf8")
        serv.send(hora2, (data))
        break
    conn.close()

