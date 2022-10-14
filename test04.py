#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

#import sqlanydb
import os
#import psycopg2
import sqlite3
from clases.cls_Bdd import BaseDD
import datetime
from clases.cls_SmartDB import Indicadores
from modulos.funciones import substr,  printlog 


printlog("Inicio .--" )

con = sqlite3.connect("SmartDB.db") 

cur = con.cursor()
res_conn = cur.execute("select Motor, Servidor, Usuario, Clave, BDD, Puerto from Tbl_Conexion where Servidor = 'Ares';") 
Motor, Servidor, Usuario, Clave, BDD, Puerto =res_conn.fetchone() 

print (Motor, Servidor, Usuario, Clave, BDD, Puerto)

res_consulta = cur.execute("select Id, Motor, Tipo, Consulta, Fecha, Tabla, Estructura from Tbl_Indicadores where Motor='MariaDB';")  
res_cons_Consulta =res_consulta.fetchall()

#Servidor='Ares2'

dbConn=BaseDD(servidor=Servidor, usuario=Usuario, clave=Clave, db=BDD, puerto=Puerto, drver='', motor='MariaDB') 

Status=Indicadores(Id=0, Motor=dbConn.Motor,conn=con)

print('Aqui 1')
dbConn.ejecutar_query('select 1 ;')

print('Aqui 2')


if dbConn.Estado==1:
    printlog ("Base de Datos Down :  Servidor ---> " + dbConn.ServidorDB + " BDD ---> " + dbConn.SchemaDBD )
    Status.insert_tbl_Estado_BDD(0, Motor,Servidor,BDD, 'DOWN')
else :
    printlog ("Base de Datos UP :  Servidor ---> " + dbConn.ServidorDB + " BDD ---> " + dbConn.SchemaDBD )
    Status.insert_tbl_Estado_BDD(0, Motor,Servidor,BDD, 'UP')
    for a in res_cons_Consulta:
        resultado=dbConn.ejecutar_query(a[3])
        id = a[0] 
        fecha_ejecucion = datetime.datetime.now()
        printlog ("Tabla--->"+ a[5])
        Ind_=Indicadores(Id=id, Motor=dbConn.Motor,conn=con)

        try:
            for exec_cons in resultado :
                Dato = [Ind_.Id, Ind_.Motor,Servidor,BDD,fecha_ejecucion ]
                for exec_y in range(Ind_.cant_campos-5):
                    Dato.append(str(exec_cons[exec_y]))
                Ind_.insert_tbl(Dato,Ind_.Id)

        except sqlite3.Error as er:
            printlog (er)
    con.close()

printlog ("Termino .-- ")