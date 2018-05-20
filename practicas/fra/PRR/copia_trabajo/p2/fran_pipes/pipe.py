import os
from pty import fork

#r, w = os.pipe()

pid = fork()
if (pid == 0):
     print('Soy hijo')

elif (pid == -1):
    print('Error')

else:
    print('Soy el padre.')