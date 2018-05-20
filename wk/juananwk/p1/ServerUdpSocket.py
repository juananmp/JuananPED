import os, sys, socket,time


s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
server_address=("127.0.0.1", 4002)
s.bind(server_address)
data, address =s.recvfrom(4096)
fecha = data.decode('utf-8')
pasa= True
while pasa:
    if fecha== "fecha":
        print(fecha)
        hora=time.strftime("%x")
        hora2=bytes(hora,"utf8")
        s.sendto(hora2,(address))
        break

    elif fecha == "hora":
        print(fecha)
        hora=time.strftime("%X")
        hora2= bytes(hora, "utf-8")
        s.sendto(hora2, (address))
        pasa = False
    elif fecha == "No":
        break
    else:
        print("Error")
        mensaje = "Error"
        s.sendto(mensaje.encode("utf-8"), address)
        pasa = False

print("Cerrando Servidor")
s.close()
