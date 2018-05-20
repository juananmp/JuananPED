import os, sys, socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
#el puerto tiene que ser distinto al del server
server_address=("127.0.0.1", 4002)
s.connect(server_address)
hora = input("Si quieres la hora recibir la hora debes escribir hora y si quieres la fecha debes escribir fecha: ")
s.sendto(bytes(hora.encode('utf-8')),('127.0.0.1',4002))
datos = s.recv(1000)
if datos.decode("utf-8") == "Error":
    print("La palabra introducida no es correcta vuelva a ejecutar el server y el cliente")
    mensaje = "No"
    s.sendto(bytes(mensaje.encode("utf-8")), ('127.0.0.1', 4002))
    s.close()
else:
    #datos=s.recv(1000)
    mensaje= "No"
    s.sendto(bytes(mensaje.encode("utf-8")), ('127.0.0.1', 4002))
    print(datos)
