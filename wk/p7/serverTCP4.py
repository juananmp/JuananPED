import os, sys, socket,select

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
s.bind(('0.0.0.0',4078))
s.listen(5)
lista_servidor=[s]
lectores_posibles=[]


while True:
    lectores_activados,_,_=select.select(lista_servidor+lectores_posibles,(),())
    #Cuando solo tengo el socket del servidor lo que hace es recibir peticiones de clientes
    #Cuando tengo los sockets de clientes, lo que hace es recibir información
    for i in lectores_activados:

        try:

            if i==s:
                scliente, addr =s.accept()
                lectores_posibles.append(scliente)

            elif i!=s:
                datos=i.recv(1024)
                if(datos==bytes("adios\r\n","utf8")):
                    scliente.close()
                    lectores_posibles.remove(scliente)
                else:
                    for o in lectores_posibles:

                        print("datos: %s" % datos)
                        o.send(datos)

        except BrokenPipeError:
            scliente.close()
            lectores_posibles.remove(scliente)
