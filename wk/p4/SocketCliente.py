import socket  
  
s = socket.socket()   
s.connect(("localhost", 9999))  
  
while True:  
      mensaje = input(">")
      men=mensaje.encode()   
      s.send(men)  
      if mensaje == "quit":  
         break  
  
print ("adios") 
  
s.close()  
