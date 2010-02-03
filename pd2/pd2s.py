#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kamila Turek"
__doc__ = """
NAME
    pd2s.py - weather server

SYNOPIS
    pd2s.py [-p PORT|--port=PORT] [-h|--help]

OPTIONS
    -h, --help
        prints this help text
    -p, --port
        sets server port
"""

import getopt
import sys
import socket
import threading
from time import sleep
from __future__ import with


cache = {'Lublin': [{'temp': '0'}, {'temp': '1'}, {'temp': '2'}, {'temp': '3'}, {'temp': '4'}, {'temp': '5'}, {'temp': '6'}],
         'Warszawa': [{'temp': '0'}, {'temp': '1'}, {'temp': '2'}, {'temp': '3'}, {'temp': '4'}, {'temp': '5'}, {'temp': '6'}],
         'Kielce': [{'temp': '0'}, {'temp': '1'}, {'temp': '2'}, {'temp': '3'}, {'temp': '4'}, {'temp': '5'}, {'temp': '6'}]}
six_hours = 60 * 60 * 6

def process_options():
    port = 9911
    server = ''

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'hp:',
                                       ['help', 'port='])
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

    return (server, port)


def get_response(period, city):
    response = 'ok '
    if period == 'prd':
        response += 'd '
        weather = cache[city][:1]
    else:
        response += 't '
        weather = cache[city]
    response += str(len(cache[city][0])) + '\n' # ilosc danych
    for day in weather:
        for key in day:
            response += key + ':' + day[key] + '\n'
    return response


class ReCache(threading.Thread):
    def __init__(self, lock):
        self.lock = lock
        self.end = False
        threading.Thread.__init__(self)

    def run(self):
        while not self.end:
            with self.lock:
                print "recache not implemented"
            sleep(six_hours)

    def stop(self):
        self.end = True


class Client(threading.Thread):
    def __init__(self, client, lock):
        self.client = client
        self.lock = lock
        threading.Thread.__init__(self)

    def run(self):
        f = self.client.makefile()
        period, city = f.readline().strip().split()
        f.close()
        with self.lock:
            response = get_response(period, city)
        self.client.sendall(response)
        self.client.close()


def main():
    lock = threading.Lock()

    threads = []
    recache = ReCache(lock)
    recache.start()

    address = process_options()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(address)
    s.listen(5)

    try:
        while True:
            client, _ = s.accept()
            t = Client(client, lock)
            t.start()
            threads.append(t)
    except KeyboardInterrupt:
        for t in threads:
            t.join()
        recache.stop()


if __name__ == "__main__":
    sys.exit(main())
