import sqlite3
from clases.cls_SmartDB import Indicadores
from modulos.funciones import substr
import random 



con = sqlite3.connect("SmartDB.db") 
cur = con.cursor()

a=Indicadores(Id=2, Motor='MariaDB',conn=con)
#a.lee_indicadores()

print(a.Tabla)

print(a.valida_exist_tabla(a.Tabla))

if a.valida_exist_tabla(a.Tabla) == 0:
    a.creaTabla(a.Tabla)


tabla= 'tbl_mdb_p001'
msg = "SELECT p.name AS col_name FROM sqlite_master m LEFT OUTER JOIN pragma_table_info((m.name)) p ON m.name <> p.name WHERE m.type = 'table' and m.name = '" + tabla + "' ORDER BY p.cid ;"

#print (msg)


#a.genera_sql_insert('tbl_mdb_p001')

msg='  Hola Como estas _  '

print(substr(msg.strip(), 0, len(msg.strip())-1))

print(a.insert)
print(a.cant_campos)

Dato= []

for x in range(6) :
    for y in range(6) :
        Dato.append((x,y, x+y, x*y))       
print (Dato)



