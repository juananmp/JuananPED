import socket, sys, select, time

socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_conexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#ojo pasar los argumentos 1 (localhost) y 2 (puerto)
socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
#se mantienen hasta 5 clientes en espera
socket_conexion.listen(5)

#uno de los requisitos es que los nicks no se repitan para ello tendremos una lista 

lista_users=[]

#rlist ahora mismo tendra el socket de conexion, que es el que usara el servidorpara arrancar
rlist = [socket_conexion]

while True:
#definimos el select

    ready_rlist, ready_wlist, ready_xlist = select.select(rlist, [],[])
#algo es el socket_conexion ahora
    for algo in ready_rlist:
#si el socket que recibimos es el de conexion:
        if algo == socket_conexion:
            print("Un cliente esta intentando conectarse")
            n_sock, addr = socket_conexion.accept()
            rlist.append(n_sock)
            n_sock.send("Introduce tu user, por favor:".encode('utf-8'))
            user = n_sock.recv(1024)
            if user in lista_users:
                n_sock.send("Este usuario ya existe intentalo con otro")
                rlist.remove(n_sock)
                algo.close()
            else:
                lista_users.append(user)
                print("El user : " + user.decode("utf-8") + "Se acaba de conectar")
                n_sock.send("Ya estas conectado, puedes empezar a chatear".encode("utf-8"))
        else: 
            mensaje = algo.recv(1024)
            if mensaje.decode("utf-8 " == "quit" or mensaje.decode("utf-8") == ""):
                rlist.remove(algo)
                algo.close()

            for user in rlist:
                if user == socket_conexion or user == algo:
                    pass
            else:
                user.send(mensaje)
 

