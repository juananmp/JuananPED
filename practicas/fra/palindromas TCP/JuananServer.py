import os,sys,socket, select

haElegidoMenu = []
haSeleccionadoNumero = []
haSeleccionadoFrase = []

def conexion(socket_conexion):
    print('Cliente conectado'+ str(socket_conexion))
    n_sock,addr= socket_conexion.accept()
    rlist.append(n_sock)
    mensaje = "Te has conectado al Servidor, escribe la palabra Menu"
    men = mensaje.encode("utf-8")
    n_sock.send(men)
def generar_respuesta(datos, elemento):
    if not (elemento in haElegidoMenu) and datos == "Menu":
        haElegidoMenu.append(elemento)
        respuesta = ("Elija una de estas opciones" + "\n" + "1. Frase" + "\n" + "2. Numero" + "\n" + "3. Exit")
    if elemento in haElegidoMenu:
        if not (elemento in haSeleccionadoNumero) and datos == "2":
            haSeleccionadoNumero.append(elemento)
#            haElegidoMenu.remove(elemento)
            respuesta = "Introduce su numero palindromo, por favor"
        elif (elemento in haSeleccionadoNumero) and not datos == "Exit":
            if str(datos) == str(datos)[::-1]:
                respuesta = "Su numero es un palindromo"
            else:
                respuesta = "Su numero no es un palindromo"
        elif not (elemento in haSeleccionadoFrase) and datos =="1":
            haSeleccionadoFrase.append(elemento)
            respuesta = "Introduce su frase palindroma, por favor"
        elif (elemento in haSeleccionadoFrase) and not datos == "Exit":
            if str(datos) == str(datos)[::-1]:
                respuesta = "Su frase es un palindromo"
            else:
                respuesta = "Su frase no es un palindromo"

        elif datos == "Exit" or datos == "3":
            if elemento in haSeleccionadoNumero:
                haSeleccionadoNumero.remove(elemento)
            if elemento in haSeleccionadoFrase:
                haSeleccionadoFrase.remove(elemento)
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
        ready_rlist, ready_wlist, ready_xlist = select.select(rlist, [], [])
        
        for elemento in ready_rlist:
#la primera vez que se conecta un cliente al servidor, se llama a socket_conexion para aceptar la conexion
            if elemento == socket_conexion:
                conexion(elemento)
            else:
                mensaje2 = elemento.recv(1024)
                datos = mensaje2.decode("utf-8")
                respuesta = generar_respuesta(datos, elemento)
                mensaje = respuesta.encode("utf-8")
                elemento.send(mensaje)
                
#                mensaje = "Te has conectado al servidor"
#                mr = mensaje.encode("utf-8")
#               elemento.send(mr)    
