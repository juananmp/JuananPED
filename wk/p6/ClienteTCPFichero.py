import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10005))
message = os.path.abspath("Texto.txt")
print(message)
s.sendall(message.encode('utf-8'))
data = s.recv(1024)
s.close()
print ('Received', data)
