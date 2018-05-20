import sys
import socket
import select
 
def cliente_chat():
#    if(len(sys.argv) < 3) :
 #       print ('Inserte localhost puerto del servidor y su nombre, gracias')
  #      sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    nombre = str(sys.argv[3])+': '
	
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # conexion con el host remoto
    try :
        s.connect((host, port))
    except :
        print( 'Imposible realizar la conexion')
        sys.exit()
     
    print ('Conectado con el servidor')
    sys.stdout.write(nombre ); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Coge la lista de sockets para leer
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # mensaje entrante desde un servidor remoto, s
                data = sock.recv(4096)
                if not data :
                    print ('\nDesconexion con el Servidor')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write(nombre); sys.stdout.flush()     
            
            else :
                # El usuario escribe mensaje
                msg = sys.stdin.readline()
                s.send(nombre+msg)
                sys.stdout.write(nombre); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(cliente_chat())
