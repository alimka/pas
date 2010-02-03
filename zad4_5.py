#!/usr/bin/python
#-*-coding:utf-8-*-

import socket
import sys

if len(sys.argv) != 2:
    sys.exit("Podałeś za mało argumentów")

tab = sys.argv[1].split('@')

port = 79

if (tab[1]):
    host = tab[1]
else:
    host = '127.0.0.1'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    if (tab[0]):
        s.send(tab[0]+'\r'+'\n')
    else:
        s.send(''+'\r'+'\n')
    data = s.recv(1024)
    while data:
        sys.stdout.write(data)
        data = s.recv(1024)
except socket.gaierror:
    sys.exit("Nie odnaleziono domeny")
