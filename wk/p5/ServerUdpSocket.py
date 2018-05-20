import os, sys, socket,time


s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
server_address=("127.0.0.1", 4002)
s.bind(server_address)
data, address =s.recvfrom(4096)

if data:
    print(data)
    hora=time.strftime("%c")
    hora2=bytes(hora,"utf8")
    s.sendto(hora2,(address))
else:
    print("Error")
