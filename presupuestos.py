#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata
import pymssql
import sys
reload(sys)
#tokens for api pipedrive and MSSQLINGENIERIA
from tokens import *

sys.setdefaultencoding("utf-8")
print("######### Importando datos de Negocios #########")

#Def para borrar tabla sql
def borrar_presupuestos(arg):
    conn = pymssql.connect(host=host,user=user,password=password,database=database)
    cur = conn.cursor()
    cur.execute('DELETE FROM [SAP].[dbo].[Presupuestos]')
    conn.commit()
    conn.close()
    return arg
def insertar(sql):
    conn = pymssql.connect(host=host,user=user,password=password,database=database)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return conn
#Switchers
def origen_propuesta(argument):
    switcher = {
        '262': "Primero",
        '263': "Complementario",
    }
    return switcher.get(argument, "nothing")
def area_contacto(argument):
    switcher = {
        '226': "Proyectos",
        '227': "Construccion",
        '228': "Mantenimiento",
        '229': "Compras sin depto. tecnico",
        '230': "Compras con depto. tecnico",
        '231': "Inversionista",
        '232': "Desconocido",
        '233': "RH",
        '234': "Proveedores",
    }
    return switcher.get(argument, "nothing")
def medio_contacto(argument):
    switcher = {
        '218': "NotificadorWeb",
        '219': "Telefono",
        '220': "Chat",
        '221': "Correo",
        '222': "Mailling",
        '223': "Recomendacion",
        '224': "TrabajoPrevio",
        '225': "Prospectacion",
    }
    return switcher.get(argument, "nothing")
def tipo_presupuestos(argument):
    switcher = {
        '215': "PT1",
        '216': "PT2",
        '217': "PT3",
    }
    return switcher.get(argument, "nothing")
def presupuestos_categorizacion(argument):
    switcher = {
        '207': "Calculo",
        '208': "ProyectosEjecutivos",
        '209': "ProyectosDeInversion",
        '210': "GerenciaDeProyectos",
        '211': "ObraEspecializada",
        '212': "Subcontratos",
        '213': "Suministros",
        '214': "INMO",
    }
    return switcher.get(argument, "nothing")

def presupuestos_estado(argument):
        switcher = {
            'won': "Cerrado",
            'lost': "Perdido",
        }
        return switcher.get(argument, "Abierto")

def presupuestos_estado_compra(argument):
        switcher = {
            '204': "Vacio",
            '205': "Activo",
            '206': "Cerrado",
        }
        return switcher.get(argument, "Vacio")
#Borramos la tabala
DelStatus = borrar_presupuestos('Borrando tabla presupuestos....')
print(DelStatus)
#Sql Injection
c = 0
cn = 0
#Iteramos para sacar todos los Registros
Paginas =  0
Limite = True
while Limite == True:

    path_url  = 'https://api.pipedrive.com/v1/deals:(id,person_id,org_id,title,9d6b02fe5f3a6926be97fe956149713d8876eb94,add_time,next_activity_date,close_time,value,8ee24c17f3ac04493089780b7cffee1512a1c134,status,5fbdf9384d1386ea81869f1916f8b5315c8de476,6a3fcf31541cf6790d804c1d3815d2a26292fcae,5fbdf9384d1386ea81869f1916f8b5315c8de476,fc28f857b56a26688545ca6f23157b3f2a906d5f,949f438cfe1937242f13455abddc2fd5ce83d8b6,5ca7ac46b820ac0bd01c58d55856386f37969ec0,6ea10f31bbceef5313534f5146886b85b58684eb,0a837de9247fbb2bce2fb666f7eb10fd83d25bab,de8fbbfc2b0c8ad81a57de2ad2c5ea0a925bed57,3425d9b6fb771c07afa9def1659582575ee77519,e66510859c41827c98571249f4d347ad2b7692fa,61261220b85aeb30bab6f426b143f9cbbf047c2c)?api_token=' + str(api_token) + '&start=' + str(Paginas) + 'limit=100'
    r=urlopen(path_url)
    data = json.loads(r.read(),encoding='utf-8',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
    Limite= data['additional_data']['pagination']['more_items_in_collection']

    for datos in data["data"]:
        if datos['person_id'] is None:
            cn = cn + 1
        else:
            if datos['org_id'] is None:
                cn = cn + 1
            else:
                #
                c = c+1;
                sql = 'INSERT INTO [SAP].[dbo].[Presupuestos] VALUES(\''
                #Id
                sql += str(datos['id']) + '\''
                #IdCliente
                if datos['person_id'] is None:
                    sql += ',\'0\''
                else:
                    if datos['person_id']['value'] == "":
                        sql += ',\'0\''
                    else:
                        sql +=',\'' + str(datos['person_id']['value']) + '\''
                #IdEmpresa
                if datos['org_id'] is None:
                    sql += ',\'0\''
                else:
                    if datos['org_id']['value'] == "":
                        sql += ',\'0\''
                    else:
                        sql +=',\'' + str(datos['org_id']['value']) + '\''
                #Referencia
                if datos['title'] == "":
                    sql += ',\'Referencia\''
                else:
                    titles = datos['title'].encode('UTF-8', 'replace')
                    titles.encode('ascii','ignore')
                    titles.encode('utf-8',errors='replace')

                    sql += ',\'' + titles + '\''
                #Direccion
                if datos['9d6b02fe5f3a6926be97fe956149713d8876eb94'] is None:
                    sql += ',\'Direccion\''
                else:
                        if datos['9d6b02fe5f3a6926be97fe956149713d8876eb94'] == '':
                            sql += ',\'Direccion\''
                        else:
                            Dir = datos['9d6b02fe5f3a6926be97fe956149713d8876eb94'].encode('UTF-8', 'replace')
                            Dir.encode('ascii','ignore')
                            Dir.encode('utf-8',errors='replace')
                            sql += ',\'' + Dir + '\''
                #FechaCreacion Negocio Creado
                if datos['add_time'] is None:
                    sql += ',\'01-01-1900\''
                else:
                    if datos['add_time'] == '':
                        sql += ',\'01-01-1900\''
                    else:
                        sql += ',\'' + datos['add_time'].encode('UTF-8', 'replace') + '\''
                #FechaMaduracion Negocio Cerrado en
                if datos['close_time'] is None:
                    sql += ',\'01-01-1900\''
                else:
                    if datos['close_time'] == '':
                        sql += ',\'01-01-1900\''
                    else:
                        sql += ',\'' + datos['close_time'].encode('UTF-8', 'replace') + '\''
                #FechaProximoContacto ya interesa
                if datos['next_activity_date'] is None:
                    sql += ',\'01-01-1900\''
                else:
                    if datos['next_activity_date'] == '':
                        sql += ',\'01-01-1900\''
                    else:
                        sql += ',\'' + datos['next_activity_date'].encode('UTF-8', 'replace') + '\''
                #Estado
                if datos['status'] == '':
                    sql += ',\'-\''
                else:
                    SEstado = presupuestos_estado(str(datos['status']))
                    sql += ',\'' + SEstado.encode('UTF-8', 'replace') + '\''
                #Bloque Sql sistema viejo Termometro,Motivos,Total,Competidor,ImporteInicial
                sql += ',\'0\',\'0\',\'0\',\'0\',\'0\''
                #Importe Final
                if datos['value'] is None:
                    sql += ',\'0\''
                else:
                    if datos['value'] == '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['value']) + '\''
                #Bloque slq del biejo sistema
                #Contribucion Brutas
                if datos['5fbdf9384d1386ea81869f1916f8b5315c8de476'] is None:
                    sql += ',\'0\''
                else:
                    if datos['5fbdf9384d1386ea81869f1916f8b5315c8de476'] ==  '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['5fbdf9384d1386ea81869f1916f8b5315c8de476']) + '\''
                #ContribucionReal
                if datos['8ee24c17f3ac04493089780b7cffee1512a1c134'] is None:
                    sql += ',\'0\''
                else:
                    if datos['8ee24c17f3ac04493089780b7cffee1512a1c134'] == '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['8ee24c17f3ac04493089780b7cffee1512a1c134']) + '\''
                #MargenReal
                if datos['5fbdf9384d1386ea81869f1916f8b5315c8de476'] is None:
                    sql += ',\'0\''
                else:
                    if datos['5fbdf9384d1386ea81869f1916f8b5315c8de476'] ==  '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['5fbdf9384d1386ea81869f1916f8b5315c8de476']) + '\''
                #Proyecto
                if datos['6a3fcf31541cf6790d804c1d3815d2a26292fcae'] is None:
                    sql += ',\'-\''
                else:
                    if datos['6a3fcf31541cf6790d804c1d3815d2a26292fcae'] == '':
                        sql += ',\'-\''
                    else:
                        sql += ',\'' + datos['6a3fcf31541cf6790d804c1d3815d2a26292fcae'].encode('UTF-8', 'replace') + '\''
                #[NoProyecto]
                if datos['0a837de9247fbb2bce2fb666f7eb10fd83d25bab'] is None:
                    sql += ',\'0\''
                else:
                    if datos['0a837de9247fbb2bce2fb666f7eb10fd83d25bab'] == '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['0a837de9247fbb2bce2fb666f7eb10fd83d25bab']) + '\''
                #[EstatusCompras]
                if datos['949f438cfe1937242f13455abddc2fd5ce83d8b6'] is None:
                    sql += ',\'-\''
                else:
                    if datos['949f438cfe1937242f13455abddc2fd5ce83d8b6'] == '':
                        sql += ',\'-\''
                    else:
                        EdoCompra = presupuestos_estado_compra(str(datos['949f438cfe1937242f13455abddc2fd5ce83d8b6']))
                        sql += ',\'' + str(EdoCompra) + '\''
                #[Categorizacion]
                if datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0'] is None:
                    sql += ',\'-\''
                else:
                    if datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0'] == '':
                        sql += ',\'-\''
                    else:
                        SCategorizacion = presupuestos_categorizacion(str(datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0']))
                        sql += ',\'' + SCategorizacion.encode('UTF-8', 'replace') + '\''
                #Bloque de sql del sistema viejo
                sql +=',\'Venta\',\'Vendedor\',\'Vista\''
                #IdAntiguo48435f4a7b83707f666bfc53ac8bec0d3b90bea5
                if datos['6ea10f31bbceef5313534f5146886b85b58684eb'] is None:
                    sql += ',\'0\''
                else:
                    if datos['6ea10f31bbceef5313534f5146886b85b58684eb'] == '':
                        sql += ',\'0\''
                    else:
                        sql += ',\'' + str(datos['6ea10f31bbceef5313534f5146886b85b58684eb']) + '\''
                #origen propuesta
                if datos['61261220b85aeb30bab6f426b143f9cbbf047c2c'] is None:
                    sql += ',\'-\''
                else:
                    if datos['61261220b85aeb30bab6f426b143f9cbbf047c2c'] == '':
                        sql += ',\'-\''
                    else:
                        origenpropuesta = origen_propuesta(datos['61261220b85aeb30bab6f426b143f9cbbf047c2c'])
                        sql += ',\'' + str(origenpropuesta) + '\''
                #area contacto
                if datos['e66510859c41827c98571249f4d347ad2b7692fa'] is None:
                    sql += ',\'-\''
                else:
                    if datos['e66510859c41827c98571249f4d347ad2b7692fa'] == '':
                        sql += ',\'-\''
                    else:
                        areacontacto = area_contacto(datos['e66510859c41827c98571249f4d347ad2b7692fa'])
                        sql += ',\'' + str(areacontacto) + '\''
                #medios contacto
                if datos['3425d9b6fb771c07afa9def1659582575ee77519'] is None:
                    sql += ',\'-\''
                else:
                    if datos['3425d9b6fb771c07afa9def1659582575ee77519'] == '':
                        sql += ',\'-\''
                    else:
                        mediocontacto = medio_contacto(datos['3425d9b6fb771c07afa9def1659582575ee77519'])
                        sql += ',\'' + str(mediocontacto) + '\''
                #tipo presupuestos
                if datos['de8fbbfc2b0c8ad81a57de2ad2c5ea0a925bed57'] is None:
                    sql += ',\'-\')'
                else:
                    if datos['de8fbbfc2b0c8ad81a57de2ad2c5ea0a925bed57'] == '':
                        sql += ',\'-\')'
                    else:
                        tipopresupuesto = tipo_presupuestos(datos['de8fbbfc2b0c8ad81a57de2ad2c5ea0a925bed57'])
                        sql += ',\'' + str(tipopresupuesto) + '\')'
                print(sql)
                insertar(sql)
    Paginas = Paginas + 100
print("######### Registros procesados a MSQLServer No.:" + str(c) + "##########")
print("######### Registros no procesados " + str(cn) + "##########")
