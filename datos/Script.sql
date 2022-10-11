
create table Tbl_Servidor (Servidor, SOP, Marca, Procesador, Nucleos, Slot_Memoria, Memoria, Almacenamiento, Modelo, Tipo);
create table Tbl_BDD (BDD, Marca, Motor, Version);
create table Tbl_Conexion (Motor, Servidor, Usuario, Clave, BDD, Puerto);
create table Tbl_Indicadores (Motor, Tipo, Consulta, Fecha);
create table Tbl_Historico_Indicadores (Motor, Tipo, Consulta, Fecha) ;


create table  Tbl_Indicadores 
( Motor, 
  Tipo, 
  Descripcion, 
  Consulta, 
  Fecha,
  Tabla, 
  Estructura
); 

insert into Tbl_Indicadores ( Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura) values
(
    1,
    'MariaDB',
    'Espacio por Base de Datos',
    'Consulta que calcula espacios por BDD',
     'SELECT
      table_schema,
      ROUND(SUM(data_length + index_length) / 1024 / 1024, 3) AS ''Database Size (MB)'',
      ROUND(SUM(data_free) / 1024 / 1024, 3) AS ''Free Space (MB)''
    FROM
      information_schema.tables
    GROUP BY
      table_schema
    ORDER BY
      2 DESC;',
    '2022-10-11',
    'tbl_mdb_p001',
    'create table tbl_mdb_p001 (table_schema,size_db, free_space)'
);

insert into Tbl_Indicadores ( id, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura) values
(
    2,
    'MariaDB',
    'Version Base de Datos',
    'Consulta de version del motor de BDD',
    'select version();',
    '2022-10-11',
    'tbl_mdb_p002',
    'create table tbl_mdb_p001 (version_motor)'
);

insert into Tbl_Indicadores (id, Motor, Tipo, Descripcion, Consulta, Fecha, Tabla,  Estructura) values
(
    3,
    'MariaDB',
    'Version Base de Datos',
    'Consulta de version del motor de BDD',
    'select version();',
    '2022-10-11',
    'tbl_mdb_p002',
    'create table tbl_mdb_p001 (version_motor)'
);

SELECT
  VERSION() as 'version',
  USER()    as  'usuario'
  CURRENT_USER() as 'usuario_actual',
  DATABASE() as 'bdd',    
  NOW() ,
  CURDATE() fecha_sistema,
  CURTIME() hora_sistema,
  UTC_DATE(),
  UTC_TIME(),
  UTC_TIMESTAMP(),
  SYSDATE(),      -- returns date of function completion
  -- PS_CURRENT_THREAD_ID(),  -- MySQL 8.0.16+
  UUID_SHORT(),   -- integer
  UUID()          -- alnum
;

(('10.6.10-MariaDB-1:10.6.10+maria~deb10', 'root@localhost', 'root@localhost', 'Prueba', datetime.datetime(2022, 10, 6, 22, 54, 21), datetime.date(2022, 10, 6), datetime.timedelta(seconds=82461), datetime.date(2022, 10, 7), datetime.timedelta(seconds=6861), datetime.datetime(2022, 10, 7, 1, 54, 21), datetime.datetime(2022, 10, 6, 22, 54, 21), 99984672963952677, 'f61611ad-45e2-11ed-8bb5-080027ef254d'),)