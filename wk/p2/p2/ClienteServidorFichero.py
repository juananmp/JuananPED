import os, sys

print "El hijo escribira un texto por la tuberia y "
print "el padre leera el texto escrito por el hijo..."

# file descriptors r, w for reading and writing
fdr, fdw = os.pipe()

processid = os.fork()
if processid:
    # This is the parent process 
    # Closes file descriptor w
    os.close(fdw)
    r = os.fdopen(fdr)
    print "El servido lee"
    file = open(str(r.read()), 'r')
    str = file.read()
    print "texto =", str
    #infile.close()
    sys.exit(0)
else:
    # This is the child process
    os.close(fdr)
    w = os.fdopen(fdw, 'w',0)
    print "Hijo escribe"
    w.write("/home/juananmp/Desktop/EjemplosPython/p2/Texto")
    w.close()
    print "Hijo cierra"
    sys.exit(0)
