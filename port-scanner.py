#!/bin/python
import sys
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("invalid")

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res = s.connect_ex((target,port))

        if res == 0:
            print("Port {} is open".format((port)))
            s.close()

except KeyboardInterrupt:
    print("Exiting")
    sys.exit()

except socket.gaierror:
    print("Hostname cannot be resolved")
    sys.exit()

except socket.error:
    print("Cannot connect to server")
    sys.exit()
