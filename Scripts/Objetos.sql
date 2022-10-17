create table Tbl_Servidor (
    Id_Servidor  INT NOT NULL AUTO_INCREMENT, 
    Servidor varchar(100) not null, 
    IP varchar(50) not null, 
    SOP varchar(100) not null,
    Marca varchar(100) not null,
    Procesador varchar(100) not null,
    Nucleos int, 
    Slot_Memoria int, 
    Memoria varchar(100) not null,
    Almacenamiento varchar(100) not null, 
    Modelo varchar(100)  null, 
    Tipo varchar(100) not null,
    PRIMARY KEY(Id_Servidor)
    );

create table Tbl_BDD (
    Id_BDD INT NOT NULL AUTO_INCREMENT,
    BDD varchar(100) not null, 
    Marca varchar(100) not null, 
    Motor varchar(100) not null, 
    Version varchar(100) not null,
    PRIMARY KEY(Id_BDD)
);


create table Tbl_Conexion 
(
    Id_Conexion INT NOT NULL AUTO_INCREMENT,
    Motor varchar(100) not null, 
    Id_Servidor int not null, 
    Usuario varchar(100) not null, 
    Clave varchar(100) not null, 
    BDD varchar(100) not null , 
    Puerto varchar(100) null,
    PRIMARY KEY(Id_Conexion)
);


create table Tbl_Indicadores 
(
    id_Indicadores INT NOT NULL AUTO_INCREMENT, 
    Motor varchar(100) not null, 
    Tipo varchar(100) not null,  
    Descripcion varchar(500) not null,
    Consulta varchar(2000)  null , 
    Fecha datetime null, 
    Tabla varchar(100)  null , 
    Estructura varchar(1000)  null , 
    PRIMARY KEY(id_Indicadores)
 );


CREATE TABLE tbl_mdb_p000 
(
    id Integer null,  
    Motor varchar(200) null , 
    Id_Servidor integer null, 
    BDD varchar(200) null,
    Fecha datetime null, 
    Estado varchar(50) null
);

create table tbl_mdb_p001 
    (
     id Integer null, 
     Motor varchar(200) null , 
     Id_Servidor integer null, 
     BDD varchar(200) null , 
     Fecha datetime null, 
     table_schema varchar(200) null ,
     size_db real, 
     free_space real
     )
     ;
     
create table tbl_mdb_p002 
    (
     id Integer null, 
     Motor varchar(200) null , 
     Id_Servidor integer null, 
     BDD varchar(200) null , 
     Fecha datetime null, 
     version_motor varchar(200) null 
     )
     ;
    
create table tbl_mdb_p003
(
     id Integer null, 
     Motor varchar(200) null , 
     Id_Servidor integer null, 
     BDD varchar(200) null , 
     Fecha datetime null, 
     VARIABLE_NAME varchar(200) null ,
     VARIABLE_VALUE real
)
;

create table tbl_mdb_p004 
(
     id Integer null, 
     Motor varchar(200) null , 
     Id_Servidor integer null, 
     BDD varchar(200) null , 
     Fecha datetime null, 
     LAST_STARTUP datetime ,
     Uptime varchar(200) null
);


CREATE FUNCTION fn_Servidor (id_serv INT) 
    RETURNS VARCHAR(100) DETERMINISTIC
BEGIN
    
    declare res char(100);
    
    select Servidor into res
    from Tbl_Servidor 
    where Id_Servidor = id_serv;
    
    return res;
    
END;