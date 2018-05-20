import os, sys
# Path to be created
path = "hourly"
try:
    os.mkfifo(path)
except OSError, e:
    print "Failed to create FIFO: %s" % e
else:
    fifo = open(path, 'w')
print "Path is created"
