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

print (dbConn.ServidorDB,dbConn.SchemaDBD, dbConn.UsuarioDB)

i=0
for a in res_cons_Consulta:
    print("Consulta : ", a[0] )
    resultado=dbConn.ejecutar_query(a[3])
    fecha_ejecucion = datetime.datetime.now()
    cur.execute("insert into Tbl_Resultados(Servidor, BDD, Motor, id_indicador, Resultados) values (?, ?, ?, ?, ?, ?)", (Servidor, BDD, Motor, fecha_ejecucion, a[0],"Consulta" ))
    print(resultado)
    i=i+1

#res_cons_Consulta.close() 

con.close()
