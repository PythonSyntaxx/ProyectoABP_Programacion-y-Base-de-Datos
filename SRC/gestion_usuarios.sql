-- 1 Crear la base de datos

CREATE DATABASE gestion_usuarios;

USE gestion_usuarios;

-- 2 Crear tabla de roles

CREATE TABLE roles (
	id_rol INT PRIMARY KEY AUTO_INCREMENT,
    rol VARCHAR (255) NOT NULL 
    );
    
-- 3 Crear tabla de usuarios

CREATE TABLE users (
	id_user INT NOT NULL  AUTO_INCREMENT,
    name VARCHAR (100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    id_rol INT NOT NULL, 
    PRIMARY KEY (id_user),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);


