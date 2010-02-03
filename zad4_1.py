#!/usr/bin/python

import socket
import sys

try:
    domena = raw_input("Podaj domene: ")
    while domena:
        try:
            ipv4 = socket.gethostbyname_ex(domena)
            for i in ipv4[2]:
                print i
            domena = raw_input("Podaj domene: ")
        except socket.gaierror:
            print "Nie znaleziono hosta."
            domena = raw_input("Podaj nowa domene: ")
except EOFError:
        sys.exit()
