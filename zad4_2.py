#!/usr/bin/python

import socket
import sys

try:
    ip = raw_input("Podaj ip:")
    while ip:
        try:
            domena = socket.gethostbyaddr(ip)
            print domena[0]
            ip = raw_input("Podaj ip:")
        except socket.gaierror:
            print "Nie znaleziono domeny"
            ip = raw_input("Podaj nowe ip: ")
except EOFError:
    sys.exit()
