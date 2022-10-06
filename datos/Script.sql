
create table Tbl_Servidor (Servidor, SOP, Marca, Procesador, Nucleos, Slot_Memoria, Memoria, Almacenamiento, Modelo, Tipo);
create table Tbl_BDD (BDD, Marca, Motor, Version);
create table Tbl_Conexion (Motor, Servidor, Usuario, Clave, BDD, Puerto);
create table Tbl_Indicadores (Motor, Tipo, Consulta, Fecha);
create table Tbl_Historico_Indicadores (Motor, Tipo, Consulta, Fecha) ;