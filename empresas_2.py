# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata
import pymssql
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print("######### Importando datos de Organizaciones #########")
#Def para borrar tabla sql
def borrar_empresas(arg):
    conn = pymssql.connect(host='DEVELOPER\MSSQLINGENIERIA',user='sistemas',password='masterMX9456',database='SAP')
    cur = conn.cursor()
    cur.execute('DELETE FROM [SAP].[dbo].[Empresas]')
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
def estdo_empresa(argument):
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

def perfil_empresa(argument):
    switcher = {
        '142': "Industrial",
        '143': "Energia",
        '144': "Comercial",
        '145': "DesarrolladoraGral",
        '146': "Buffete-Arq-Ing",
        '147': "Hotelero",
        '148': "FondoDeInversion",
        '149': "GerenciaDeProyectos",
        '150': "Retail",
        '151': "Entretenimiento",
        '152': "Salud",
        '153': "Vivienda",
        '154': "ConstructoraGral",
        '155': "Gobierno",
        '156': "PersonaFisica",
        '157': "InfraestructuraPublica",
    }
    return switcher.get(argument, "nothing")
#Borramos la tabala
DelStatus = borrar_empresas('Borrando tabla empresas....')
print(DelStatus)
#Sql Injection
c = 0
#Iteramos para sacar todos los Registros
Paginas =  0
Limite = True
while Limite == True:
    Paginas += 100
    path_url  = 'https://api.pipedrive.com/v1/organizations:(id,name,52d696d9b7a5bb5720c17ca1b711061693067b6e,88f1db137d17d589d2335cf77ef4f06d3ac30809,30d6284d10ed91edf62d222d51d441f2a5bca1fc,73f181bd11548510a4dcfadafc036ff5dcdde8ae,dd8264651561775a4d9eb4f843811bc599649cb6,add_time,22b81f40f537c0d5b2aabe3041fd6df1967dac52,ee637749af8f57299eb455821a26dce35cf928ba)?api_token=84ec27e18fd9bd90a10cdcdcfefd91dab0bbe02d&start=' + str(Paginas) + 'limit=100'
    r=urlopen(path_url)
    data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
    Limite= data['additional_data']['pagination']['more_items_in_collection']
    for datos in data["data"]:
        c = c+1;
        sql = 'INSERT INTO [SAP].[dbo].[Empresas] VALUES (\''
        #Id
        sql += str(datos['id']) + '\''
        #Empresa
        sql += ',\'' + datos['name'] + '\''
		#R. Social
        if datos['52d696d9b7a5bb5720c17ca1b711061693067b6e'] == '':
            sql += ',\'R.Social\''
        else:
            sql += ',\'' + unicode(datos['52d696d9b7a5bb5720c17ca1b711061693067b6e']) + '\''
		#RFC
        if datos['88f1db137d17d589d2335cf77ef4f06d3ac30809'] == '':
            sql += ',\'RFC\''
        else:
            sql += ',\'' + str(datos['88f1db137d17d589d2335cf77ef4f06d3ac30809']) + '\''
		#Dir Fiscal
        if datos['30d6284d10ed91edf62d222d51d441f2a5bca1fc'] == '':
            sql += ',\'Dir\''
        else:
            sql += ',\'' + unicode(datos['30d6284d10ed91edf62d222d51d441f2a5bca1fc']) + '\''
		#Dir Entrega campo vacio
        sql += ',\'D\''
        #Beneficio
        sql += ',\'B\''
       #Giro
        if datos['73f181bd11548510a4dcfadafc036ff5dcdde8ae'] == '':
            sql += ',\'G\''
        else:
            giro = perfil_empresa(unicode(datos['73f181bd11548510a4dcfadafc036ff5dcdde8ae']))
            sql += ',\'' + giro + '\''
		#Web
        if datos['dd8264651561775a4d9eb4f843811bc599649cb6'] == '':
            sql += ',\'w\''
        else:
            sql += ',\'' + unicode(datos['dd8264651561775a4d9eb4f843811bc599649cb6']) + '\''
		#Datos vacio
        sql += ',\'ProyectoInstalaciones\',\'ProyectoEstructural\',\'Suministros\',\'SistemasConstructivos\',\'Arquitectura\''
        #Fecha Registro
        if datos['add_time'] == '':
            sql += ',\'01-01-1900\''
        else:
            sql += ',\'' + str(datos['add_time']) + '\''
		#Estado Rep
        if datos['22b81f40f537c0d5b2aabe3041fd6df1967dac52'] == '':
            sql += ',\'-Estado-\''
        else:
			Edo = estdo_empresa(unicode(datos['22b81f40f537c0d5b2aabe3041fd6df1967dac52']))
			sql += ',\'' + Edo +'\''
        print(sql)
print("######### Registros proesados a MSQLServer No.:" + str(c) + "##########")