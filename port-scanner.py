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

# /////////////////////////////////////////////////////////////////////////////

from socket import *

def conScan(tgtHost, tgtPort):
     try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print(tgtPort + ' Open')
        connskt.close()
    except:
        print(tgtPort + ' Closed')

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot be resolve " + tgtPort)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('Results for ' + tgtName[0])
    except:
        print('Results for ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning: ' + tgtPort)
        conScan(tgtHost, int(tgtPorts))

    # if __name__ == '__main__':
    #     portScan({Url}, [{Ports}])
