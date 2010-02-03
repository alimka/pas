#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print sys.argv

if len(sys.argv) != 3:
    print "Musisz podać dokładnie dwa argumenty: plik, który chcesz kopiować i plik do którego chcesz kopiować"
    sys.exit()

try:
    plik_do_zapisu = open(sys.argv[2], 'w')
except IndexError:
    print "Nie można otworzyć pliku do zapisu, sprawdź czy ma nadane odpowiednie prawa"
    sys.exit()

with open(sys.argv[1]) as file:
    for line in file:
        plik_do_zapisu.write(line)

plik_do_zapisu.close()
