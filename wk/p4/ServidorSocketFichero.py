import socket

HOST = 'localhost'
PORT = 9869
ADDR = (HOST,PORT)
serv = socket.socket()

serv.bind(ADDR)
serv.listen(10)

print ('listening ...')

while True:
    conn, addr = serv.accept()
    print ('client connected ... ', addr)
    while True:
        data = conn.recv(10000)
        myfile = open('Texto.txt', 'rb')
        contenido = myfile.read()
        conn.send(contenido)
        print ('writing file ....')
        break
    conn.close()
    break
print ('client disconnected')
