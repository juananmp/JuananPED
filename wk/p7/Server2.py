import socket
import time

server_address = ("127.0.0.1", 5000)
clientes = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(server_address)
#configurar el servidor para que sea nonblocking
#lo ponemos a 0, esto significa que cuando intente recibir desde no se bloqueara solo intente y tome datos del stream sino hay nada ahi entonces mostrara un error

quitting = False
print("El Servidor se ha iniciado")

while not quitting:
    try:
        data, addr =s.recvfrom(4096)
        da = data.decode()
#si uno de los clientes manda Quit se quitara el servidor
        if da == "Quitt":
            quitting = True
        if addr not in clients:
#si la direccion del cliente no esta en la lista clients, entonces la registramos
            clients.append(addr)
        print(time.ctime(time.time())+ str(adr) + ": : " + str(da))
#para el resto de clientes vamos a enviarles a todos los mensajes
 #       for client in clients:
#            s.sendto(str(da), client)
    except:
        pass
s.close()


        
