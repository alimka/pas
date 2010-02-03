#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
    print "Musisz podać dokładnie jeden parametr, który jest nazwą pliku muzycznego"
    sys.exit()

try:
    mp3 = open(sys.argv[1])
except IOError:
    print "Nie ma takiego pliku" , sys.argv[1]

mp3.seek(-128, 2)

if mp3.read(3) == 'TAG':
    name = mp3.read(30).strip()
    artist = mp3.read(30).strip()
    album = mp3.read(30).strip()
    year = mp3.read(4).strip()
    comment = mp3.read(30).strip()
    gatunek = mp3.read(1).strip()
    print name, " dupa ", artist, " dupa ", album, " dupa ", year, " dupa ", comment, " dupa ", ord(gatunek), "dupa"
