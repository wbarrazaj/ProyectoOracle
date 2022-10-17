
-- Carga Tbl_Servidor

insert into Tbl_Servidor 
(Servidor,IP,SOP,Marca,Procesador,Nucleos,Slot_Memoria,Memoria,Almacenamiento,Modelo,Tipo) 
values (
'Ares','193.168.1.159','Linux','VM','VM',1,1,'1 GB','100 GB',null,'Virtual'
);

insert into Tbl_Servidor 
(Servidor,IP,SOP,Marca,Procesador,Nucleos,Slot_Memoria,Memoria,Almacenamiento,Modelo,Tipo) 
values (
'Apolo','193.168.1.155','Linux','VM','VM',1,1,'1 GB','100 GB',null,'Virtual'
);

commit;

-- Carga TBL_BDD

insert into Tbl_BDD (BDD,Marca,Motor,Version) 
values ('Prueba','MariaDB','MariaDB','10.6.10');
commit;


-- Carga Tbl_Conexion 

insert into Tbl_Conexion (Motor,Id_Servidor,Usuario,Clave,BDD,Puerto) 
values
('MARIADB',1,'monitor','Emilita01','mysql','3306')
;

insert into Tbl_Conexion (Motor,Id_Servidor,Usuario,Clave,BDD,Puerto) 
values
('MARIADB',2,'monitor','Emilita01','mysql','3306')
;

commit;

-- Carga Tbl_Indicadores 

insert into Tbl_Indicadores 
(
    Motor,
    Tipo,
    Descripcion,
    Consulta,
    Fecha,
    Tabla,
    Estructura
)
Values 
(
    'MariaDB',
    'Espacio por Base de Datos',
    'Consulta que calcula espacios por BDD',
    "SELECT
        table_schema,
        ROUND(SUM(data_length + index_length) / 1024 / 1024, 3) AS 'Database Size (MB)',
        ROUND(SUM(data_free) / 1024 / 1024, 3) AS 'Free Space (MB)'
        FROM
        information_schema.tables
        GROUP BY
        table_schema
        ORDER BY
        2 DESC;",
    '2022-10-11',
    'tbl_mdb_p001',
    "create table tbl_mdb_p001 
        (
        id Integer null, 
        Motor varchar(200) null , 
        Id_Servidor integer null, 
        BDD varchar(200) null , 
        Fecha datetime null, 
        table_schema varchar(200) null ,
        size_db real, 
        free_space real
        )"
);

commit;


insert into Tbl_Indicadores 
(
    Motor,
    Tipo,
    Descripcion,
    Consulta,
    Fecha,
    Tabla,
    Estructura
)
Values 
(
    'MariaDB',
    'Version Base de Datos',
    'Consulta de version del motor de BDD',
    "select version();",
    '2022-10-11',
    'tbl_mdb_p002',
    "create table tbl_mdb_p002 
        (
        id Integer null, 
        Motor varchar(200) null , 
        Id_Servidor integer null, 
        BDD varchar(200) null , 
        Fecha datetime null, 
        version_motor varchar(200) null 
        )"
);
commit;


insert into Tbl_Indicadores 
(
    Motor,
    Tipo,
    Descripcion,
    Consulta,
    Fecha,
    Tabla,
    Estructura
)
Values 
(
    'MariaDB',
    'Variables Mysql',
    'Consulta de Variables de BDD Mysql',
    "select VARIABLE_NAME,VARIABLE_VALUE
    from information_schema.GLOBAL_STATUS
    where VARIABLE_NAME in
    (
    'Com_analyze',
    'Com_optimize',
    'Com_select',
    'Conexiones',
    'Innodb_rows_deleted',
    'Innodb_rows_inserted',
    'Innodb_rows_read',
    'Innodb_rows_updated',
    'Select_full_join',
    'Select_full_range_join',
    'Select_range',
    'Select_range_check',
    'Select_scan',
    'Slow_queries',
    'Sort_merge_passes',
    'Sort_range',
    'Sort_rows',
    'Sort_scan',
    'Preguntas',
    'Innodb_row_lock_time',
    'Table_locks_immediate',
    'Table_locks_waited',
    'Aborted_clients',
    'Aborted_connects',
    'Threads_created',
    'Threads_running',
    'Innodb_data_writes',
    'Innodb_dblwr_writes',
    'Innodb_log_write_requests',
    'Innodb_log_writes',
    'Innodb_pages_written',
    'Created_tmp_disk_tables',
    'Created_tmp_tables',
    'Innodb_buffer_pool_pages_data',
    'Innodb_buffer_pool_pages_total',
    'Innodb_buffer_pool_read_requests',
    'Innodb_buffer_pool_reads',
    'Opened_tables',
    'Opened_table_definitions',
    'Qcache_hits',
    'innodb_buffer_pool_hits',
    'innodb_buffer_pool_hit_rate',
    'innodb_buffer_pool_usage',
    'query_cache_hit_rate',
    'innodb_datafile_writes_to_disk',
    'innodb_rows_changed',
    'active_transactions',
    'innodb_deadlocks',
    'innodb_lock_timeouts',
    'innodb_row_lock_waits'
    )
    ;",
    '2022-10-11',
    'tbl_mdb_p003',
    "create table tbl_mdb_p003
    (
        id Integer null, 
        Motor varchar(200) null , 
        Id_Servidor integer null, 
        BDD varchar(200) null , 
        Fecha datetime null, 
        VARIABLE_NAME varchar(200) null ,
        VARIABLE_VALUE real
    )"
);
commit;

insert into Tbl_Indicadores 
(
    Motor,
    Tipo,
    Descripcion,
    Consulta,
    Fecha,
    Tabla,
    Estructura
)
Values 
(
    'MariaDB',
    'Variables Mysql',
    'Consulta de Variables de BDD Mysql',
    "select
    DATE_SUB(now(), INTERVAL variable_value SECOND) as LAST_STARTUP ,
    TIME_FORMAT(SEC_TO_TIME(VARIABLE_VALUE ),'%Hh %im') as Uptime
    from information_schema.GLOBAL_STATUS
    where VARIABLE_NAME = 'Uptime'
    ;",
    '2022-10-11',
    'tbl_mdb_p004',
    "create table tbl_mdb_p004 
    (
        id Integer null, 
        Motor varchar(200) null , 
        Id_Servidor integer null, 
        BDD varchar(200) null , 
        Fecha datetime null, 
        LAST_STARTUP datetime ,
        Uptime varchar(200) null
    )"
);
commit;
