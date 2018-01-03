# JsonToMSSQL

> This script was make for can sync all registers that be in the data base in Pepedrive
,only  download the Tables Clients,Cuotes and Companys, with the Json of this datas
Sync our old system made in MSSQL.

### Tools used in this project

- Python 2.7.11
- json
- urllib2
- unicodedata
- pymssql
- sys


### Descriptions of scripts

**Main** : This script can run all scripts and is used by that bot run the routine.

**Presupuestos** : This script get all deals of pipe drive and update the table SAP.Presupuestos.

**Empresas** : This script get all Companies of pipe drive and update the table SAP.Emresas..

**Clientes** :This script get all Clients of pipe drive and update the table SAP.Clientes.


![How is works](https://github.com/ArmandAguilar/JsonToMSSQL/blob/master/Diagram/JsonToMSSQL.png)
