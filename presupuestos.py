#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata

print("######### Importando datos de Negocios #########")
path_url  = ''
r=urlopen(path_url)
data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)

#Sql Injection
c = 0
for datos in data["data"]:
    c = c+1;
    sql = str(c) + '.-INSERT INTO [SAP].[dbo].[Presupuestos] VALUES(\''
    #Id
    sql += str(datos['id']) + '\''
    #IdCliente
    if datos['person_id'] == "":
        sql += ',\'0\''
    else:
        sql += ',\'0\''
    #IdEmpresa
    if datos['org_id'] == '':
        sql += ',\'0\''
    else:
        sql += ',\'' + str(datos['org_id']['value']) + '\''
    #Referencia
    if datos['title']:
        sql += ',\'Referencia\''
    else:
        sql += ',\'' + str(datos['title']) + '\''
    #Direccion
    if datos['9d6b02fe5f3a6926be97fe956149713d8876eb94'] == '':
        sql += ',\'Direccion\''
    else:
        sql += ',\'' + unicode(datos['9d6b02fe5f3a6926be97fe956149713d8876eb94']) + '\''
    #FechaCreacion
    if datos['add_time'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['add_time']) + '\''
    #FechaMaduracion
    if datos['close_time'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['close_time']) + '\''
    #FechaProximoContacto]
    if datos['next_activity_date'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['next_activity_date']) + '\''
    #Bloque Sql sistema viejo
    sql += ',\'Estado\',\'Termometro\',\'Motivos\',\'Total\',\'Competidor\',\'ImporteInicial\''
    #Importe Final
    if datos['value'] == '':
        sql += ',\'0\''
    else:
        sql += ',\'' + str(datos['value']) + '\''
    #Bloque slq del biejo sistema
    sql += ',\'ContribucionBruta\''
    #ContribucionReal
    if datos['8ee24c17f3ac04493089780b7cffee1512a1c134'] == '':
        sql += ',\'0\''
    else:
        sql += ',\'' + str(datos['8ee24c17f3ac04493089780b7cffee1512a1c134']) + '\''
    #MargenReal
    if datos['5fbdf9384d1386ea81869f1916f8b5315c8de476'] ==  '':
        sql += ',\'0\''
    else:
        sql += ',\'' + str(datos['8ee24c17f3ac04493089780b7cffee1512a1c134']) + '\''
    print(sql)
print("######### Registros proesados a MSQLServer No.:" + str(c) + "##########")
