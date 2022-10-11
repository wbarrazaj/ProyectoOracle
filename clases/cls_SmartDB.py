import sqlite3


class Indicadores():
    def __init__(self, Motor, Id, conn):
            self.Id = Id
            self.Motor =  Motor
            self.Tipo = ''
            self.Descripcion = ''
            self.Consulta = '' 
            self.Fecha = ''
            self.Tabla = ''
            self.Estructura = ''
            self.conn=conn

      
    def __valida_exist_tabla(self, tabla):
        cons="select 1 FROM sqlite_master where type='table' and tbl_name='"+ tabla+"'"
        cur = self.conn.cursor() 
        resp = cur.execute(cons)

        if resp==1:
            return 1
        else :
            return 0
        pass

    def __creaTabla ():
        pass 

    def lee_indicadores (self):
        id_= str(self.Id)
        cur = self.conn.cursor() 
        consult= "select Id, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura from Tbl_Indicadores where Id =" + id_ + " and Motor ='" + self.Motor + "';"
        resp = cur.execute(consult)
        self.Id, self.Motor, self.Tipo, self.Descripcion, self.Consulta, self.Fecha, self.Tabla , self.Estructura = resp.fetchone()

    def genera_sql_insert():
        pass
