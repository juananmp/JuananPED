import socket, sys, os, select

sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

dir_server=(sys.argv[1], int(sys.argv[2]))
sock.connect(dir_server)

while True:
    ready_rlist, ready_wlist, ready_xlist = select.select([sock, sys.stdin],[],[])
    for elemento in ready_rlist:
        if elemento == sys.stdin:
            mensaje = input()
            if mensaje == 'exit' or mensaje == '':
                sock.send(mensaje.encode('utf-8'))
                sock.close()
                break

            else:
                sock.send(mensaje.encode('utf-8'))
        else:
            mensaje = sock.recv(1024)
            print(mensaje.decode('utf-8'))

