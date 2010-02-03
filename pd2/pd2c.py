#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kamila Turek"
__doc__ = """
NAME
    pd2c.py - weather client

SYNOPIS
    pd2c.py [-p PORT|--port=PORT] [-s SERVER|--server=SERVER] [-h|--help]

OPTIONS
    -h, --help:
        prints this help text
    -p, --port:
        sets server port
    -s, --server:
        sets server address
"""

import sys
import logging
import getopt
import socket

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
log = logging.getLogger('server')

def process_options():
    port = 9911
    server = 'matrix.umcs.lublin.pl'

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'hp:s:',
                                       ['help', 'port=', 'server='])
    except getopt.GetoptError, err:
        print str(err)
        print __doc__
        return sys.exit(1)

    for o, a in opts:
        if o in ('-h', '--help'):
            print __doc__
            return 0
        elif o in ('-p', '--port'):
            port = int(a)
        elif o in ('-s', '--server'):
            server = a

    return (server, port)

def get_request():
    while 1:
        print "\nPogoda:\n  1.) jedniodniowa\n  2.) dwudniowa\nPodaj numer:",
        okres = raw_input()
        if okres == '1': okres = 'prd'; break
        elif okres == '2': okres = 'prt'; break
        else: print 'Błędna opcja, spróbuj jeszcze raz.'

    while 1:
        lista_miast = ['Lublin', 'Warszawa', 'Kielce']
        print "\nMiasto:"
        for n in range(len(lista_miast)):
            print "%i.) %s" % (n, lista_miast[n])
        print "Podaj numer:",
        try:
            miasto = lista_miast[input()]
            break
        except (NameError, IndexError):
            print 'Błędna opcja, spróbuj jeszcze raz.'

    return okres + ' ' + miasto + '\n'



def main():
    server, port = process_options()
    request = get_request()

    #log.debug(request)
    #log.debug('port: %s, server: %s' % (port, server))

    s = socket.socket()
    s.connect((server, port))
    s.sendall(request)

    response = ''
    while 1:
        data = s.recv(1024)
        if not data: break
        response += data

    print response

    s.close()


if __name__ == "__main__":
    sys.exit(main())
