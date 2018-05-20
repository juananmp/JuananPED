import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10005))
s.listen(10)

conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    myfile = open('Texto.txt', 'rb')
    contenido = myfile.read()
    conn.sendall(contenido)
    print("writing file...")
    break
conn.close()
print("Cliente disconnected")
