import socket
import time

server_address = ("127.0.0.1", 5000)
clientes = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
s.bind(server_address)
#configurar el servidor para que sea nonblocking
#lo ponemos a 0, esto significa que cuando intente recibir desde no se bloqueara solo intente y tome datos del stream sino hay nada ahi entonces mostrara un error
 

s.setblocking(0)

quitting = False
print("El Servidor se ha iniciado")

while not quitting:
    try:
        data, addr =s.recvfrom(4096)
#si uno de los clientes manda Quit se quitara el servidor
        if "Quit" in str(data):
            quitting = True
        if addr not in clientes:
#si la direccion del cliente no esta en la lista clients, entonces la registramos
            clientes.append(addr)
        print(time.ctime(time.time())+ str(adr) + ": : " + str(data))
#para el resto de clientes vamos a enviarles a todos los mensajes
        for client in clientes:
            s.sendto(str(data).encode('utf-8'), client)
    except:
        pass
s.close()


        
