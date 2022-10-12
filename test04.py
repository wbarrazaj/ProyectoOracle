#import sqlanydb
import os
#import psycopg2
import sqlite3
from clases.cls_Bdd import BaseDD
import datetime
from clases.cls_SmartDB import Indicadores
from modulos.funciones import substr
import random 


con = sqlite3.connect("SmartDB.db") 

cur = con.cursor()
res_conn = cur.execute("select Motor, Servidor, Usuario, Clave, BDD, Puerto from Tbl_Conexion where Servidor = 'Ares';") 
Motor, Servidor, Usuario, Clave, BDD, Puerto =res_conn.fetchone() 


res_consulta = cur.execute("select Id, Motor, Tipo, Consulta, Fecha, Tabla, Estructura from Tbl_Indicadores where Motor='MariaDB';")  
res_cons_Consulta =res_consulta.fetchall()

Servidor='Ares2'


dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor='MariaDB') 

#print (dbConn)

#print (dbConn.ServidorDB,dbConn.SchemaDBD, dbConn.UsuarioDB)

for a in res_cons_Consulta:
    #print("Consulta : ", a[0] )
    resultado=dbConn.ejecutar_query(a[3])
    #print(resultado)
    id = a[0] 
    fecha_ejecucion = datetime.datetime.now()
    print (a[5])
    Dato = []
    Ind_=Indicadores(Id=id, Motor=dbConn.Motor,conn=con)

    try:
        cur.execute("INSERT INTO Tbl_Resultados VALUES(?, ?, ?, ?, ?, ?)", (Servidor, BDD, Motor, fecha_ejecucion, id, str(resultado)))
        con.commit()
        i = 0
        for exec_cons in resultado :
            for exec_y in range(Ind_.cant_campos):
                print (exec_cons, exec_y) 
        i = i + 1


        print (Dato)


    except sqlite3.Error as er:
        print(er)

    #cur.execute("insert into Tbl_Resultados(Servidor) values (?);", (Servidor))
    
res_ejec_consulta = cur.execute("select * from Tbl_Resultados;")  
res_ej_Consulta =res_ejec_consulta.fetchall()


print (res_ej_Consulta)

"""
for b in res_ej_Consulta: 
    print(b)



#res_cons_Consulta.close() 
"""

con.close()
