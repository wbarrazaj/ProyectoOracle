from readline import insert_text
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

      
    def valida_exist_tabla(self, tabla):
        cons="select count(*) FROM sqlite_master where type='table' and tbl_name='"+ tabla+"';"
        cur = self.conn.cursor() 
        resp = cur.execute(cons)
        r=resp.fetchone()

        if r[0]==1:
            return 1
        else :
            return 0

    def creaTabla (self, tabla):
        id_= str(self.Id)
        cur = self.conn.cursor() 
        consult= "select Estructura from Tbl_Indicadores where Id =" + id_ + " and Motor ='" + self.Motor + "';"
        resp = cur.execute(consult)
        a=resp.fetchone() 
        print(consult)
        cre_table=a[0]+ ';'
        print(cre_table)
        cur.execute(cre_table)

    def lee_indicadores (self):
        id_= str(self.Id)
        cur = self.conn.cursor() 
        consult= "select Id, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura from Tbl_Indicadores where Id =" + id_ + " and Motor ='" + self.Motor + "';"
        resp = cur.execute(consult)
        self.Id, self.Motor, self.Tipo, self.Descripcion, self.Consulta, self.Fecha, self.Tabla , self.Estructura = resp.fetchone()

    def genera_sql_insert(self, tabla):
        cur = self.conn.cursor() 
        consulta="SELECT p.name AS col_name FROM sqlite_master m LEFT OUTER JOIN pragma_table_info((m.name)) p ON m.name <> p.name WHERE m.type = 'table' and m.name = '" + tabla + "' ORDER BY p.cid ;"
        
        print(consulta)
        
        resp = cur.execute(consulta)
        campos = ''
        campos2 = ''

        for a in resp.fetchall():
            campos = campos + a[0] + ','
            campos2 = campos2 + '?,'
        

        lin=len(campos.strip())-1
        print (campos[0:lin])
        lin2=len(campos2.strip())-1
        print (campos2[0:lin2])

        ins_txt = 'inster into ' + tabla + '(' + campos[0:lin] + ') values (' + campos2[0:lin2] + ')'
        print(ins_txt)








