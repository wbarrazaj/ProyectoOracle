#import sqlanydb
import os
import psycopg2
import sqlite3
from clases.cls_Bdd import BaseDD

con = sqlite3.connect("SmartDB.db") 

cur = con.cursor()
res_conn = cur.execute("select Motor, Servidor, Usuario, Clave, BDD, Puerto from Tbl_Conexion where Servidor = 'Ares';") 
Motor, Servidor, Usuario, Clave, BDD, Puerto =res_conn.fetchone() 
#print(Motor, Servidor, Usuario, Clave, BDD, Puerto) 

print("")

res_consulta = cur.execute("select Motor, Tipo, Consulta, Fecha from Tbl_Indicadores where Motor='MariaDB';")  
res_cons_Consulta =res_consulta.fetchall()

print(res_cons_Consulta[0])

Servidor='Ares2'

con.close()

dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor='MariaDB') 

#print (dbConn)

print (dbConn.ServidorDB,dbConn.SchemaDBD, dbConn.UsuarioDB)

resultado=dbConn.ejecutar_query(res_cons_Consulta[2])

print(resultado)

