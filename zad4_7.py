#! /usr/bin/python
#-*- coding:utf-8 -*-

import socket
import sys

if len(sys.argv) != 2:
    print "Nieprawidłowa liczba argumentów"
    sys.exit()

host = ''
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
ip = {'':''}
while 1:
    (conn, addr) = s.accept()
    adres = addr[0]

    # to co ma wyświetlić serwer:
    out = sys.stdout.write
    # sys.stdout.write(addr[0]+'\n')
    out(adres+'\n')

    hostname = socket.gethostbyaddr(adres)
    sys.stdout.write(hostname[0]+'\n')

    if ip.get(adres) != None:
        ip[adres] += 1
    else:
        ip[adres] = 1
    out(ip[adres])

    conn.close()
