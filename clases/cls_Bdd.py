import pyodbc 
import pymysql
import psycopg2
from modulos.funciones import substr,  printlog 



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
        self.Estado = 0
    
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
            try:
                conn = pymysql.connect(
                                host=self.ServidorDB,
                                user=self.UsuarioDB,
                                password=self.PasswordDB,
                                db=self.SchemaDBD
                                    ) 
            except ValueError as err:
                printlog("Algo salio Mal : Servidor ---> " + self.ServidorDB + " BDD --->" + self.SchemaDBD)
                printlog(err) 
                self.Estado = 1 




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
        try:
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
                resultado=cursor.fetchall()
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
                printlog("Otra Motor")
        except pymysql.err.OperationalError as err:
                printlog("Algo salio Mal : Servidor ---> " + self.ServidorDB + " BDD --->" + self.SchemaDBD)
                if err.args[0] == 2003:
                    printlog(str(err.args[0]) + "Can't connect to MySQL server" )    
                else :
                    printlog(str(err.args[0]) + "Error to MySQL server" )

                self.Estado = 1 
                resultado = ''

        return resultado

    def chk_default(self):
  
        try:
            self.ejecutar_query('select 1 ;')
            res = True

        except:
            res = False
            
        return res


