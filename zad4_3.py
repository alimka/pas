#!/usr/bin/python
#-*-coding:utf-8-*-

import socket
import sys, os

try:
    if len(sys.argv) != 3:
        print "Podałeś za mało argumentów"
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    print data
    s.close()
except socket.gaierror:
    print "Nie znaleziono hosta"
    sys.exit()
