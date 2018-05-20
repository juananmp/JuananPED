import sys, socket, select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

def Servidor_chat():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # anadir el socket servidor de lectura
    SOCKET_LIST.append(server_socket)
 
    print ("El chat del servidor se inicia en el puerto " + str(PORT))
 
    while 1:

     
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # Nueva conexion
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print ("Cliente (%s, %s) conectado" % addr)
                 
                broadcast(server_socket, sockfd, "[%s:%s]se unido a la conversacion \n" % addr)
             
            # Mensaje del nuevo cliente
            else:
                # Datos recividos del cliente. 
                try:
                    # Datos del socket
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # Hay algo en el socket
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # eliminar soket   
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # No hay datos
                        broadcast(server_socket, sock, "Cliente (%s, %s) se desconecto\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Cliente (%s, %s) se desconecto\n" % addr)
                    continue

    server_socket.close()
    
# transmitir mensajes de chat para todos los clientes conectados
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # enviar mensaje
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # Se a roto la comunicacion
                socket.close()
                # Eliminamos el socket
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(Servidor_chat()) 
