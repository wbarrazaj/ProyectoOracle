import sqlite3
from clases.cls_SmartDB import Indicadores


#con = sqlite3.connect("SmartDB.db") 
#cur = con.cursor()

#a=Indicadores(Id=1, Motor='MariaDB',conn=con)
#a.lee_indicadores()

#print(a.Estructura)


aaa='create table tbl_mdb_p001 (table_schema,size_db, free_space)'
l=len(aaa)
print(aaa)
print(l)

aa=aaa.split(',')

print(aa)