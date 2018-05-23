import os, sys, socket, time, select

haElegidoMenu = []

def conexion(socket_conexion):
    print("Cliente conectado ... ")
    n_sock, addr = socket_conexion.accept()
    rlist.append(n_sock)
    mensaje = "Te has conectado al Servidor, escribe la palabra Menu"
    men = mensaje.encode("utf-8")
    n_sock.send(men)

def cerrar(elemento):
    rlist.remove(elemento)
    # haElegidoMenu.remove(elemento)
    elemento.close()

def generar_respuesta(datos, elemento):
    if not (elemento in haElegidoMenu) and datos == "Menu":
        haElegidoMenu.append(elemento)
        respuesta = ("Elija una de estas opciones" + "\n" + "1. Fecha" + "\n" + "2. Hora" + "\n" + "3. Exit")
    
    elif elemento in haElegidoMenu and datos == "1":
        hora = time.strftime("%x")
                
        respuesta = "La fecha es: "+ hora

    elif elemento in haElegidoMenu and datos =="2":
        respuesta = "Su hora es " + time.strftime("%X")
         
    elif datos == "Exit" or datos == "3":
        haElegidoMenu.remove(elemento)
        respuesta = "Para continuar probando, Escriba nuevamente Menu"

    else:
        respuesta = "Escribiste mal la palabra Menu, por favor vuelve a escribirla"
    return respuesta


if __name__ == '__main__':
    socket_conexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_conexion.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    socket_conexion.bind((sys.argv[1], int(sys.argv[2])))
    socket_conexion.listen(5)

    rlist = [socket_conexion]
    while True:
        ready_rlist, _, ready_xlist = select.select(rlist, [], [])

        for elemento in ready_rlist:
#la primera vez que se conecta un cliente al servidor, se llama a socket_conexion para aceptar la conexion
            if elemento == socket_conexion:
                conexion(elemento)
            else:
                mensaje2 = elemento.recv(1024)
                datos = mensaje2.decode("utf-8")
                if datos:
                    respuesta = generar_respuesta(datos, elemento)
                    mensaje = respuesta.encode("utf-8")
                    elemento.send(mensaje)
                else:
                    cerrar(elemento)

