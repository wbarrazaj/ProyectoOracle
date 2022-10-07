#import sqlanydb
import os
import psycopg2
import sqlite3
from clases.cls_Bdd import BaseDD
import datetime


con = sqlite3.connect("SmartDB.db") 

cur = con.cursor()
res_conn = cur.execute("select Motor, Servidor, Usuario, Clave, BDD, Puerto from Tbl_Conexion where Servidor = 'Ares';") 
Motor, Servidor, Usuario, Clave, BDD, Puerto =res_conn.fetchone() 
#print(Motor, Servidor, Usuario, Clave, BDD, Puerto) 

print("")

res_consulta = cur.execute("select Id, Motor, Tipo, Consulta, Fecha from Tbl_Indicadores where Motor='MariaDB';")  
res_cons_Consulta =res_consulta.fetchall()



Servidor='Ares2'


dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor='MariaDB') 

#print (dbConn)

#print (dbConn.ServidorDB,dbConn.SchemaDBD, dbConn.UsuarioDB)

for a in res_cons_Consulta:
    #print("Consulta : ", a[0] )
    resultado=str(dbConn.ejecutar_query(a[3]))
    #print(resultado)
    id = a[0] 
    fecha_ejecucion = datetime.datetime.now()
    #cur.execute("insert into Tbl_Resultados(Servidor, BDD, Motor, Fecha, id_indicador, Resultados) values (?, ?, ?, ?, ?, ?);", (Servidor, BDD, Motor, fecha_ejecucion, id, str(resultado)))
    cur.executemany("insert into Tbl_Resultados(Servidor, BDD, Motor, Fecha, id_indicador, Resultados) values (?, ?, ?, ?, ?, ?)", (Servidor, BDD, Motor, fecha_ejecucion, id, resultado))
    #cur.execute("insert into Tbl_Resultados(Servidor) values (?);", (Servidor))
    
res_ejec_consulta = cur.execute("select * from Tbl_Resultados where Motor='MariaDB';")  
res_ej_Consulta =res_ejec_consulta.fetchall()


print (res_ejec_consulta.fetchall())

"""
for b in res_ej_Consulta: 
    print(b)



#res_cons_Consulta.close() 
"""

con.close()
