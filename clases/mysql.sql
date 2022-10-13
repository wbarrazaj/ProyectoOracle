mysql 


Mediciones de base de datos

SELECT  table_schema "Base de Datos",  sum( data_length + index_length ) / 1024 / 1024 "Tamao en MB" FROM   information_schema.TABLES GROUP BY table_schema;



espacio libre 

SELECT table_schema "Base de datos",         sum( data_length + index_length ) / 1024 / 1024 "Tamaño (MB)",         sum( data_free )/ 1024 / 1024 "Espacio libre (MB)"         FROM information_schema.TABLES         GROUP BY table_schema;


Tamaño de una tabla 

SELECT table_name AS "Tables", 
    round(((data_length + index_length) / 1024 / 1024), 2) "Size in MB"  
FROM information_schema.TABLES  
--WHERE table_schema = "factura" 
ORDER BY (data_length + index_length) DESC;



	titulo text,
	autor text,
	editorial text,
	precio real,
	cantidad integer






sudo mysqladmin version
sudo systemctl status mariadb




SELECT a.alertid,a.clock,a.sendto,a.subject,a.message,a.s tatus,a.retries,a.error,a.userid,a.actionid,a.medi atypeid,a.alerttype FROM alerts a WHERE EXISTS (SELECT NULL FROM events e,functions f,items i,hosts_groups hgg JOIN rights r ON r.id=hgg.groupid AND r.groupid=14 WHERE a.eventid=e.eventid AND e.objectid=f.triggerid AND f.itemid=i.itemid AND i.hostid=hgg.hostid GROUP BY f.triggerid HAVING MIN(r.permission)>0 AND MAX(r.permission)>="2") AND EXISTS (SELECT NULL FROM actions aa WHERE a.actionid=aa.actionid AND aa.eventsource="0") AND (a.userid IS NULL OR EXISTS (SELECT NULL FROM users_groups ug WHERE ug.userid=a.userid AND ug.usrgrpid=14)) ORDER BY a.clock DESC LIMIT 25;



SELECT object_type,
           CONCAT(object_schema, '.', object_name) AS objects,
           enabled,
           timed
      FROM performance_schema.setup_objects
     
     ORDER BY object_type, objects;


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDG09oaM9zO9gmA1gmFiZqJ6hmq2GZGuoJfofTQaGTZCRzbl34vKXamQWlLvnVEHoY7488m/8zIyHMDNMlHL+FRFxgzR39l1jTE53QGIMuxt88/5X37HWPVQYf4gMWJ+FAk8jyDXphq/laHEsNvollcSoIttqjNwn4gr7dEmW08LLLH0EwTZzRMz/H1q2i/M6wwLYcAx+iKaJg19B3xyA4hRqFqLFYbT3gCF30ZKZRgh/Pe5y6Hwv/FpTDtdjSkHduFsCHx3Sv228KlxNX5Lm44QiHJ1QfMId5EjNauzyWUHoKQH9a+ZJLXQVposdL3cYMi4kqTYeh8LFCTrIY+jTdMBcvLwF14fQx5ym1JsquaeEwgvAYmBIbHZoqZUbeWL3HEyA8Oe8bPdfy2DGQ8n4MlkEYmIDjKSqoOZuhm1GJiwtDgnip2EY+CvnC8eRhdV030q7fatq5DTXWZ2aPZKxT7+ssCAfQAshxa/fdYP2Bj3RBttgoCoWdOAxh1SHUqUY8= wbarraza@Ares


SELECT * 
FROM information_schema.tables 
WHERE table_comment LIKE '%invalid%';





(('localhost', 'mariadb.sys', 0, 0, 'Y'), ('localhost', 'mysql', 0, 0, 'N'), ('localhost', 'root', 0, 0, 'N'))
(('localhost', 'mariadb.sys', 0, 0, 'Y'), ('localhost', 'mysql', 0, 0, 'N'), ('localhost', 'root', 0, 0, 'N'))

(('10.6.10-MariaDB-1:10.6.10+maria~deb10',),)

(('localhost', 'mariadb.sys', 0, 0, 'Y'), ('localhost', 'mysql', 0, 0, 'N'), ('localhost', 'root', 0, 0, 'N'))

(('10.6.10-MariaDB-1:10.6.10+maria~deb10', 'root@localhost', 'root@localhost', 'Prueba', datetime.datetime(2022, 10, 6, 22, 57, 27), datetime.date(2022, 10, 6), datetime.timedelta(seconds=82647), datetime.date(2022, 10, 7), datetime.timedelta(seconds=7047), datetime.datetime(2022, 10, 7, 1, 57, 27), datetime.datetime(2022, 10, 6, 22, 57, 27), 99984672963952679, '6518aa95-45e3-11ed-8bb5-080027ef254d'),)


(
 ('localhost', 'mariadb.sys', 0, 0, 'Y'), 
 ('localhost', 'mysql', 0, 0, 'N'), 
 ('localhost', 'root', 0, 0, 'N')
)


(('10.6.10-MariaDB-1:10.6.10+maria~deb10',),)

(
    ('mysql', Decimal('2.547'), Decimal('0.000')), 
    ('information_schema', Decimal('0.203'), Decimal('0.000')), 
    ('sys', Decimal('0.031'), Decimal('0.000')), 
    ('Prueba', Decimal('0.016'), Decimal('0.000')), 
    ('performance_schema', Decimal('0.000'), Decimal('0.000'))
)


(('mysql', Decimal('2.547'), Decimal('0.000')), ('information_schema', Decimal('0.203'), Decimal('0.000')), ('sys', Decimal('0.031'), Decimal('0.000')), ('Prueba', Decimal('0.016'), Decimal('0.000')), ('performance_schema', Decimal('0.000'), Decimal('0.000')))



=SUMAR.SI.CONJUNTO('Lorena'!$P$20:$P$36;'Lorena'!$B$20:$B$36;Octubre!E$1) + SUMAR.SI.CONJUNTO('Stephanie'!$P$20:$P$36;'Stephanie'!$B$20:$B$36;Octubre!E$1)

=SUMAR.SI.CONJUNTO(Lorena!$E$20:$E$36;Lorena!$B$20:$B$36;Octubre!E$1)+SUMAR.SI.CONJUNTO(Stephanie!$E$20:$E$36;Stephanie!$B$20:$B$36;Octubre!E$1)


=SUMAR.SI.CONJUNTO(Lorena!$J$20:$J$36;Lorena!$B$20:$B$36;Octubre!E$1)+SUMAR.SI.CONJUNTO(Stephanie!$J$20:$J$36;Stephanie!$B$20:$B$36;Octubre!E$1) 


=SUMAR.SI.CONJUNTO(Lorena!$I$20:$I$36;Lorena!$B$20:$B$36;Octubre!E$1)+SUMAR.SI.CONJUNTO(Stephanie!$I$20:$I$36;Stephanie!$B$20:$B$36;Octubre!E$1)

SUMAR.SI.CONJUNTO(Lorena!$F$20:$F$36;Lorena!$B$20:$B$36;Octubre!E$1)+SUMAR.SI.CONJUNTO(Stephanie!$F$20:$F$36;Stephanie!$B$20:$B$36;Octubre!E$1)


N° Operaciones SA
--------------------
=CONTAR.SI.CONJUNTO(Lorena!$J$20:$J$36;Lorena!$B$20:$B$36;Octubre!E$1)+CONTAR.SI.CONJUNTO(Stephanie!$J$20:$J$36;Stephanie!$B$20:$B$36;Octubre!E$1) 


=SUMAR.SI.CONJUNTO(Lorena!$F$20:$F$36;Lorena!$B$20:$B$36;Octubre!E$1)+SUMAR.SI.CONJUNTO(Stephanie!$F$20:$F$36;Stephanie!$B$20:$B$36;Octubre!E$1)



SELECT
  schemas.name AS SchemaName,
  objects.name AS TableName,
  CASE WHEN dm_db_partition_stats.index_id = 1 THEN 'Clustered Index' ELSE 'Heap' END AS TableType,
  dm_db_partition_stats.row_count
FROM sys.dm_db_partition_stats
INNER JOIN sys.objects
ON objects.object_id = dm_db_partition_stats.object_id
INNER JOIN sys.schemas
ON schemas.schema_id = objects.schema_id
WHERE objects.is_ms_shipped =
AND objects.type_desc = 'USER_TABLE'
AND dm_db_partition_stats.index_id IN (1);

#### Uptime BDD ### 

select TIME_FORMAT(SEC_TO_TIME(VARIABLE_VALUE ),'%Hh %im')  as Uptime 
from information_schema.GLOBAL_STATUS 
where VARIABLE_NAME='Uptime'

select *
from information_schema.GLOBAL_STATUS 
where VARIABLE_NAME in ('Memory_used','Connections','Cpu_time','Threads_running','Threads_created','Threads_connected')


select *
from information_schema.GLOBAL_STATUS 
where VARIABLE_NAME in ('Innodb_rows_deleted','Innodb_rows_inserted','Innodb_rows_read','Innodb_rows_updated')
;

select *
from information_schema.GLOBAL_STATUS 
where VARIABLE_NAME in ('Innodb_dblwr_writes','Innodb_data_writes','Innodb_log_write_requests','Innodb_log_writes','Innodb_pages_written');


select *
from information_schema.GLOBAL_STATUS 
where VARIABLE_NAME in ('Com_analyze');


id, Motor, Servidor, BDD,Fecha, VARIABLE_NAME,VARIABLE_VALUE

0,5,10,15,20,25,30,35,40,45,50,55,60 * * * * /home/wbarraza/Trabajo/ProyectoOracle/test04.py 

test04.py 