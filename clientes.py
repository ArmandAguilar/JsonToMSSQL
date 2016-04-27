#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata

print("######### Importando datos de personas #########")
path_url  = 'https://api.pipedrive.com/v1/persons:(id,org_id,name,phone)?api_token=84ec27e18fd9bd90a10cdcdcfefd91dab0bbe02d'
r=urlopen(path_url)
data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
#Sql Injection
c = 0

for datos in data["data"]:
    c = c+1;
    sql = str(c) + '.-INSERT INTO [SAP].[dbo].[Clientes] (\''
    #Id
    sql += str(datos['id']) + '\''
    #IdEmpresa
    sql += str(datos['org_id']['value']) + '\''
    #Nombre
    sql += ',\'' + datos['name'] + '\''
    #Bloque sql
    sql += ',\'ApellidoP\',\'ApellidoM\''
    #Telefono
    sql += ',\'' + unicode(datos['phone'][0]['value']) + '\''
    print(sql)

print("######### Registros Procesador a MSQLServer No.:" + str(c) + "##########")
