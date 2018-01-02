#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata
import pymssql
import sys
import os
reload(sys)
#tokens for api pipedrive and MSSQLINGENIERIA
from tokens import *
sys.setdefaultencoding("utf-8")

import empresas
import clientes
import presupuestos
