import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10002))
message = 'Hello world'
s.sendall(message.encode('utf-8'))
data = s.recv(1024)
s.close()
print ('Received', repr(data))
