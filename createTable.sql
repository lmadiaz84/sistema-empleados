create database if not exists empleados;

use empleados;

DROP TABLE `empleados`.`empleados`;

create table empleados(
	id int auto_increment,
    nombre varchar(255),
    correo varchar(255),
    foto varchar(5000),
    primary key (id)
);

insert into empleados (nombre,correo,foto)
values('Mario','mario@email.com','fotomario.jpg');

select * from empleados; 
