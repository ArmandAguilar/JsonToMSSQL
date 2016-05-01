#!/user/bin python
# -*- coding: utf-8 -*-
import json
from urllib2 import urlopen
import unicodedata

print("######### Importando datos de Negocios #########")
path_url  = 'https://api.pipedrive.com/v1/deals:(id,person_id,org_id,title,9d6b02fe5f3a6926be97fe956149713d8876eb94,add_time,next_activity_date,close_time,value,8ee24c17f3ac04493089780b7cffee1512a1c134,fc28f857b56a26688545ca6f23157b3f2a906d5f,949f438cfe1937242f13455abddc2fd5ce83d8b6,5fbdf9384d1386ea81869f1916f8b5315c8de476,6a3fcf31541cf6790d804c1d3815d2a26292fcae,5ca7ac46b820ac0bd01c58d55856386f37969ec0,status)?api_token=84ec27e18fd9bd90a10cdcdcfefd91dab0bbe02d'
r=urlopen(path_url)
data = json.loads(r.read(),encoding='latin-1',cls=None,object_hook=None, parse_float=None,parse_int=None, parse_constant=None,object_pairs_hook=None)
#Switchers
def presupuestos_categorizacion(argument):
    switcher = {
        '207': "Calculo",
        '208': "ProjectosEjecutivos",
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
    #FechaCreacion Negocio Creado
    if datos['add_time'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['add_time']) + '\''
    #FechaMaduracion Negocio Cerrado en
    if datos['close_time'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['close_time']) + '\''
    #FechaProximoContacto] ya interesa
    if datos['next_activity_date'] == '':
        sql += ',\'01-01-1900\''
    else:
        sql += ',\'' + unicode(datos['next_activity_date']) + '\''
    #Estado
    if datos['status'] == '':
        sql += ',\'-\''
    else:
        SEstado = presupuestos_estado(str(datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0']))
        sql += ',\'' + SEstado + '\''
    #Bloque Sql sistema viejo Termometro,Motivos,Total,Competidor,ImporteInicial
    sql += ',\'0\',\'0\',\'0\',\'0\',\'0\''
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
        sql += ',\'' + str(datos['5fbdf9384d1386ea81869f1916f8b5315c8de476']) + '\''
    #Proyecto
    if datos['6a3fcf31541cf6790d804c1d3815d2a26292fcae']:
        sql += ',\'-\''
    else:
        sql += ',\'' + unicode(datos['6a3fcf31541cf6790d804c1d3815d2a26292fcae']) + '\''
    #[NoProyecto]
    if datos['fc28f857b56a26688545ca6f23157b3f2a906d5f'] == '':
        sql += ',\'0\''
    else:
        sql += ',\'' + str(datos['fc28f857b56a26688545ca6f23157b3f2a906d5f']) + '\''
    #[EstatusCompras]
    if datos['949f438cfe1937242f13455abddc2fd5ce83d8b6'] == '':
        sql += ',\'-\''
    else:
        sql += ',\'' + str(datos['949f438cfe1937242f13455abddc2fd5ce83d8b6']) + '\''
    #[Categorizacion]
    if datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0'] == '':
        sql += ',\'-\''
    else:
        SCategorizacion = presupuestos_categorizacion(str(datos['5ca7ac46b820ac0bd01c58d55856386f37969ec0']))
        sql += ',\'' + SCategorizacion + '\''
    #Bloque de sql del sistema viejo
    sql +='\'Venta\',\'Vendedor\',\'Vista\')'
    print(sql)
print("######### Registros proesados a MSQLServer No.:" + str(c) + "##########")
