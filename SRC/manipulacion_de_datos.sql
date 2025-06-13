USE gestion_usuarios;
--  Insertar roles

INSERT INTO roles(rol) VALUES ("admin"), ("estandar")
;

-- Insertar un nuevo usuario
INSERT INTO users (name, email, password, id_rol)
VALUES ('usuario1', 'usuario1@gmail.com', 'contrasena123', 1);

SELECT * FROM users;

-- Ver todos los usuarios
SELECT u.id_user, u.name, u.email, r.rol
FROM users u
JOIN roles r ON u.id_rol = r.id_rol;

-- Actualizar datos de un usuario
UPDATE users
SET name = 'nombre_actualizado', password = 'nueva_contrasena'
WHERE email = 'correo@ejemplo.com';

-- Cambiar el rol de un usuario
UPDATE users
SET id_rol = 1
WHERE email = 'correo@ejemplo.com';

-- Eliminar un usuario
DELETE FROM users
WHERE id_user = 10;
