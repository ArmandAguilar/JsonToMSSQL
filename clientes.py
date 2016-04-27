#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata

print("######### Importando datos de personas #########")
path_url  = '
r=urlopen(path_url)
data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
#Def de campos varibles
def estdo_personal(argument):
    switcher = {
        '172': "Aguascalientes",
        '173': "Baja California",
        '174': "Baja California Sur",
        '175': "Campeche",
        '176': "Chiapas",
        '177': "Chihuahua",
        '178': "Coahuila",
        '179': "Colima",
        '180': "CDMX",
        '181': "Durango",
        '182': "Estado de Mexico",
        '183': "Guanajuato",
        '184': "Guerrero",
        '185': "Hidalgo",
        '186': "Jalisco",
        '187': "Michoacan",
        '189': "Morelos",
        '190': "Nayarit",
        '191': "Nuevo Leon",
        '192': "Oaxaca",
        '193': "Puebla",
        '194': "Queretaro",
        '195': "Quintana Roo",
        '196': "San Luis Potosi",
        '197': "Sinaloa",
        '198': "Sonora",
        '199': "Tabasco",
        '200': "Tamaulipas",
        '201': "Tlaxcala",
        '202': "Veracruz",
        '203': "Yucatan",
        '204': "Zacatecas",
    }

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
    #Bloque sql del  viejo sistema
    sql += ',\'ApellidoP\',\'ApellidoM\''
    #Telefono
    sql += ',\'' + unicode(datos['phone'][0]['value']) + '\''
    #Bloque sql del viejo sistema
    sql += ',\'Extencio\',\'Telefono2\',\'Extencion2\',\'Telefono3\',\'Extncion3\''
    sql += ',\'Fax\',\'ExtencionFax\',\'Radio\',\'ExtencionRadio\',\'Celular\''
    #Email
    sql += ',\'' + str(datos['email'][0]['value']) + '\''
    #Bloque sql
    sql += 'emial2'
    #Puesto
    sql += ',\'' + unicode(datos['4ec550c8ad97ef93d2206d97a89b5042a287f360']) + '\''
    #Tratamiento
    sql += ',\'' + unicode(datos['10c6f29db285091a1d2854ff95fc5f864233905d']) + '\''
    #Calificacion
    sql += ',\'' + unicode(datos['17852a8bfe7875c8426908547a6746954920495f']) + '\''
    #Fecha de registro
    sql += ',\'' + str(datos['add_time']) + '\''
    #Bloque de  sql viejo sistema
    sql += ',\'FormaContacto\''
    #Disc
    sql += ',\'' + unicode(datos['0f2ec4fcdff4df19ba746a04903303ea21948924']) + '\''
    #Estado
    if unicode(datos['23f6f926a83f8c72a845c09920ca22dc194fb35a']) == '':
        sql += ',\'Estado\''
    else:
        Edo = estdo_personal(datos['23f6f926a83f8c72a845c09920ca22dc194fb35a'])
        sql += ',\'' + str(Edo) + '\''
    print(sql)

print("######### Registros Procesador a MSQLServer No.:" + str(c) + "##########")
