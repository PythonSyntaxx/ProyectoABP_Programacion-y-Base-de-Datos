CREATE DATABASE gestion_usuarios;

USE gestion_usuarios;

CREATE TABLE roles (
	id_rol INT PRIMARY KEY AUTO_INCREMENT,
    rol VARCHAR (255) NOT NULL 
    );

CREATE TABLE users (
	id_user INT NOT NULL  AUTO_INCREMENT,
    name VARCHAR (100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    id_rol INT NOT NULL, 
    PRIMARY KEY (id_user),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

INSERT INTO roles(rol) VALUES ("admin"), ("estandar")
;
INSERT INTO users (name, email, password, id_rol)
VALUES ("testeo", "testeo@gmail.com", "1234", 2)
;

SELECT u.id_user, u.name, u.email, r.rol 
FROM users u 
JOIN roles r ON u.id_rol = r.id_rol;

SELECT u.id_user, u.name, u.email, r.rol 
FROM users u 
JOIN roles r ON u.id_rol = r.id_rol
WHERE email = ""
;

UPDATE users 
SET password =""
WHERE email =""
;

UPDATE users
SET id_rol=""
WHERE email = "";

DELETE FROM users
WHERE id_user = ""
;



