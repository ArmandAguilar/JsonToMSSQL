#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata

print("######### Importando datos de organizaciones #########")
path_url  = 'https://api.pipedrive.com/v1/organizations:(id,name,52d696d9b7a5bb5720c17ca1b711061693067b6e,88f1db137d17d589d2335cf77ef4f06d3ac30809,30d6284d10ed91edf62d222d51d441f2a5bca1fc,73f181bd11548510a4dcfadafc036ff5dcdde8ae,dd8264651561775a4d9eb4f843811bc599649cb6,add_time,22b81f40f537c0d5b2aabe3041fd6df1967dac52,ee637749af8f57299eb455821a26dce35cf928ba)?api_token=84ec27e18fd9bd90a10cdcdcfefd91dab0bbe02d'
r=urlopen(path_url)
data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)

print(data["success"])
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
        '120': "Estado de Mexico",
        '121': "Guanajuato",
        '122': "Guerrero",
        '123': "Hidalgo",
        '124': "Jalisco",
        '125': "Michoacan",
        '126': "Morelos",
        '127': "Nayarit",
        '128': "Nuevo Leon",
        '129': "Oaxaca",
        '130': "Puebla",
        '131': "Queretaro",
        '132': "Quintana Roo",
        '133': "San Luis Potosi",
        '134': "Sinaloa",
        '135': "Sonora",
        '136': "Tabasco",
        '137': "Tamaulipas",
        '138': "Tlaxcala",
        '139': "Veracruz",
        '140': "Yucatan",
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
#Sql Injection
c = 0
for datos in data["data"]:
    c = c+1;
    sql = str(c) + '.-INSERT INTO [SAP].[dbo].[Empresas] VALUES (\''
    #Id
    sql += str(datos['id']) + '\''
    #Empresa
    sql += ',\'' + datos['name'] + '\''
    #R. Social
    if datos['52d696d9b7a5bb5720c17ca1b711061693067b6e'] == '':
        sql += ',\'R.Social-Vacio\''
    else:
        sql += ',\'' + datos['52d696d9b7a5bb5720c17ca1b711061693067b6e'] + '\''
    #RFC
    if datos['88f1db137d17d589d2335cf77ef4f06d3ac30809'] == '':
        sql += ',\'RFC-Vacio\''
    else:
        sql += ',\'' + str(datos['88f1db137d17d589d2335cf77ef4f06d3ac30809']) + '\''
    #Dir Fiscal
    if datos['30d6284d10ed91edf62d222d51d441f2a5bca1fc'] == '':
        sql += ',\'Dir. Fiscal\''
    else:
        sql += ',\'' + unicode(datos['30d6284d10ed91edf62d222d51d441f2a5bca1fc']) + '\''
    #Dir Entrega campo vacio
    sql += ',\'Dir-Entrega \''
    #Beneficio
    sql += ',\'Beneficios\''
    #Giro
    if datos['73f181bd11548510a4dcfadafc036ff5dcdde8ae'] == '':
        sql += ',\'Giro-Vacio\''
    else:
        giro = perfil_empresa(datos['73f181bd11548510a4dcfadafc036ff5dcdde8ae'])
        sql += ',\'' + giro + '\''
    #Web
    if datos['dd8264651561775a4d9eb4f843811bc599649cb6'] == '':
        sql += ',\'web\''
    else:
        sql += ',\'' + str(datos['dd8264651561775a4d9eb4f843811bc599649cb6']) + '\''
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
        Edo = estdo_empresa(datos['22b81f40f537c0d5b2aabe3041fd6df1967dac52'])
        sql += ',\'' + Edo + '\''
    #Bloque de sql
    sql += ',\'Telefono\',\'Extencion\',\'Telefono2\',\'Extencion2\',\'Telefono3\',\'Extencion3\',\'0\''
    sql += ',\'0\',\'0\',\'01-01-1900\',\'0\',\'0\''
    sql += ',\'0\',\'01-01-1900\',\'0\',\'0\',\'0\''
    sql += ',\'01-01-1900\',\'0\',\'0\',\'0\',\'01-01-1900\''
    sql += ',\'0\',\'0\',\'0\',\'01-01-1900\',\'Potencial1\''
    sql += ',\'Observaciones1\',\'01-01-1900\',\'Protencial2\',\'Observaciones2\',\'01-01-1900\',\'Potencial3\',\'Observaciones3\',\'01-01-1900\''
    #Penticla 4
    if datos['ee637749af8f57299eb455821a26dce35cf928ba'] == "":
        sql += '\'Potencial4\''
    else:
        sql += ',\'' + str(datos['ee637749af8f57299eb455821a26dce35cf928ba']) + '\''
    #Bloque de sql
    sql += ',\'Observaciones4\',\'01-01-1900\',\'Potencial5\',\'Observaciones19\',\'Involucramiento1\',\'Observaciones5\''
    sql += ',\'01-01-1900\',\'Involucramiento2\',\'Observaciones6\',\'01-01-1900\',\'Involucramiento3\',\'Observaciones7\',\'01-01-1900\''
    sql += ',\'Involucramiento4\',\'Observaciones8\',\'01-01-1900\',\'Involucramiento5\',\'Observaciones9\''
    sql += ',\'01-01-1900\',\'Riesgo1\',\'Observaciones10\',\'01-01-1900\',\'Riesgo2\',\'Observaciones11\''
    sql += ',\'01-01-1900\',\'Riesgo3\',\'Observaciones12\',\'01-01-1900\',\'Beneficio1\',\'Observaciones13\''
    sql += ',\'01-01-1900\',\'Beneficio2\',\'Observaciones14\',\'01-01-1900\',\'Beneficio3\',\'Observaciones15\''
    sql += ',\'01-01-1900\',\'Beneficio4\',\'Observaciones16\',\'01-01-1900\',\'Beneficio5\',\'Observaciones17\''
    sql += ',\'01-01-1900\',\'Beneficio6\',\'Observaciones18\',\'01-01-1900\',\'Beneficio7\''
    sql += ',\'Observaciones20\',\'VendedorPreferente\',\'0\',\'0\',\'0\',\'0\')'
    print(sql)
print("######### Registros Procesador a MSQLServer " + str(c) + "##########")
