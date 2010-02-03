#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket
import sys

if len(sys.argv) != 2:
    print "Nieprawidlowa liczba argumentów"
    sys.exit()

host = '' # socket.gethostname()
port = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
(conn, addr) = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()
