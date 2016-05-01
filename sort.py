#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata
paginaInicial =0
paginadoAvance = 100

while True:
    paginaInicial = paginaInicial + paginadoAvance
    if paginaInicial<10000:
        print(paginaInicial)
