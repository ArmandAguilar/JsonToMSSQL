#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata
import pymssql
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print("######### Importando datos de Personas #########")
#Def para borrar tabla sql
def borrar_clientes(arg):
    conn = pymssql.connect(host='DEVELOPER\MSSQLINGENIERIA',user='sistemas',password='masterMX9456',database='SAP')
    cur = conn.cursor()
    cur.execute('DELETE FROM [SAP].[dbo].[Clientes]')
    conn.commit()
    conn.close()
    return arg
def insertar(sql):
    conn = pymssql.connect(host='DEVELOPER\MSSQLINGENIERIA',user='sistemas',password='masterMX9456',database='SAP')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return conn
#Def de campos varibles
def estdo_personal(argument):
    switcher = {
        '110': "Aguascalientes",
        '111': "Baja California",
        '112': "Baja California Sur",
        '113': "Campeche",
        '114': "Chiapas",
        '115': "Chihuahua",
        '116': "Coahuila",
        '117': "Colima",
        '118': "CDMX",
        '119': "Durango",
        '120': "Estado de México",
        '121': "Guanajuato",
        '122': "Guerrero",
        '123': "Hidalgo",
        '124': "Jalisco",
        '125': "Michoacán",
        '126': "Morelos",
        '127': "Nayarit",
        '128': "Nuevo León",
        '129': "Oaxaca",
        '130': "Puebla",
        '131': "Queretaro",
        '132': "Quintana Roo",
        '133': "San Luis Potosí",
        '134': "Sinaloa",
        '135': "Sonora",
        '136': "Tabasco",
        '137': "Tamaulipas",
        '138': "Tlaxcala",
        '139': "Veracruz",
        '140': "Yucatán",
        '141': "Zacatecas",
    }
    return switcher.get(argument, "nothing")
#Borramos la tabala
DelStatus = borrar_clientes('Borrando tabla clientes....')
print(DelStatus)
#Sql Injection
c = 0
#Iteramos para sacar todos los Registros
Paginas =  0
Limite = True
while Limite == True:
    Paginas += 100
    path_url  = 'https://api.pipedrive.com/v1/persons:(id,org_id,name,phone,email,4ec550c8ad97ef93d2206d97a89b5042a287f360,10c6f29db285091a1d2854ff95fc5f864233905d,17852a8bfe7875c8426908547a6746954920495f,add_time,0f2ec4fcdff4df19ba746a04903303ea21948924,23f6f926a83f8c72a845c09920ca22dc194fb35a)?api_token=84ec27e18fd9bd90a10cdcdcfefd91dab0bbe02d&start=' + str(Paginas) + 'limit=100'
    r=urlopen(path_url)
    data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
    Limite= data['additional_data']['pagination']['more_items_in_collection']

    for datos in data["data"]:
        c = c+1;
        sql ='INSERT INTO [SAP].[dbo].[Clientes] VALUES(\''
        #Id
        sql += str(datos['id']) + '\''
        #IdEmpresa
        if datos['org_id'] is None:
            sql += ',\'0\''
        else:
            if datos['org_id']['value'] == "":
                sql += ',\'0\''
            else:
                sql +=',\'' + str(datos['org_id']['value']) + '\''
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
        sql += ',\'emial2\''
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
        #Bloque sql del viejo sistema
        sql += ',\'0\',\'0\',\'0\',\'0\''
        sql += ',\'0\',\'0\',\'0\')'
        print(sql)
        insertar(sql)
print("######### Registros proesados a MSQLServer No.:" + str(c) + "##########")
