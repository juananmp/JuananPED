import socket
import threading
import time

#vamos a crear un lock, esto lo que hara es parar el programa cuando se intenta coger el output de la pantalla al mismo tiempo

tLock = threading.Lock()
#vamos a crear una variable shutdown que le dira al hilo que haga shutdown cuando el programa se cierre/salga

shutdown = False

#ahora vamos a definir la funcion del thread

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            time.sleep(0.1)
        finally:
            tLock.release()
host = '127.0.0.1'
#igualarlo a 0 significa que va a poder coger cualquier puerto libre en el ordenador

port = 0

server = ('localhost', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))
s.setblocking(0)
#vamos a crear nuestro hilo receptor
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

alias = input("Name: ")
message = input(alias + "-> ")
while message != 'q':
    if message != '':
        envio = alias + ": " + message
        s.sendto(str(envio).encode('utf-8'), server)
        #por si quiere enviar mas mensajes
        tLock.acquire()
        message = input (alias + "-> ")
        tLock.release()
        time.sleep(0.2)
shutdown = True
rT.join()
s.close()

