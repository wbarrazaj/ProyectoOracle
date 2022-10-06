import pyodbc 
import pymysql
import psycopg2



class BaseDD():
    """
    Server class de Conexion.
    __conectar    : metodo de conexion.
    """
    def __init__(self, servidor, usuario, clave, db, puerto, drver , motor ):
        self.ServidorDB = servidor 
        self.UsuarioDB =  usuario
        self.PasswordDB = clave
        self.SchemaDBD = db
        self.Port = puerto 
        self.Driver = drver
        self.Motor = motor
    
    def conectar(self):
        if self.Motor == 'Sybase': 
            conn = pyodbc.connect(
                                    driver=self.Driver, 
                                    server=self.ServidorDB , 
                                    database=self.SchemaDBD ,
                                    port = self.Port,
                                    uid=self.UsuarioDB, 
                                    pwd=self.PasswordDB
                                    )
        elif self.Motor in ('Mysql','MariaDB'):
            conn = pymysql.connect(
                                    host=self.ServidorDB,
                                    user=self.UsuarioDB,
                                    password=self.PasswordDB,
                                    db=self.SchemaDBD
                                    ) 

        elif self.Motor=='Postgres':
            conn = psycopg2.connect(
                                    user=self.UsuarioDB,
                                    password=self.PasswordDB,
                                    host=self.ServidorDB,
                                    port=self.Port,
                                    database=self.SchemaDBD
                                    )
        return conn

    def ejecutar_query(self, query):
        conn=self.conectar()
        #print(self.Motor)
        if self.Motor == 'Sybase':
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
        elif self.Motor in ('Mysql','MariaDB'):
            cursor = conn.cursor()
            cursor.execute(query)
            resultado=cursor.fetchone()
            #print(">>>>>>>>>>> "+resultado)
            conn.commit()
            conn.close()
        elif self.Motor == 'Postgres':
            cursor = conn.cursor()
            cursor.execute(query)
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
            conn.commit()
            conn.close()
        else:
            print("Otra Motor")
        return resultado

    def chk_default(c):
        res = True
        try:
            c.query('select 1')
            c.use_result()
        except:
            res = False
            
        return res


