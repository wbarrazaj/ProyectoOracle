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

for a in res_cons_Consulta:
    resultado=dbConn.ejecutar_query(a[3])
    id = a[0] 
    fecha_ejecucion = datetime.datetime.now()
    print (a[5])
    Ind_=Indicadores(Id=id, Motor=dbConn.Motor,conn=con)

    try:
        #cur.execute("INSERT INTO Tbl_Resultados VALUES(?, ?, ?, ?, ?, ?)", (Servidor, BDD, Motor, fecha_ejecucion, id, str(resultado)))
        #con.commit()
        i = 0
        for exec_cons in resultado :
            Dato = [Ind_.Id, Ind_.Motor,Servidor,BDD,fecha_ejecucion ]
            for exec_y in range(Ind_.cant_campos-5):
                Dato.append(str(exec_cons[exec_y]))
            Ind_.insert_tbl(Dato,Ind_.Id)

    except sqlite3.Error as er:
        print(er)
    
#res_ejec_consulta = cur.execute("select * from Tbl_Resultados;")  
#res_ej_Consulta =res_ejec_consulta.fetchall()

con.close()
