## Modelo Relacional

### Tabla: roles
| Campo   | Tipo     | Clave  | Restricciones          |
|---------|----------|--------|------------------------|
| id_rol  | INTEGER  | PK     | NOT NULL, UNIQUE       |
| rol     | VARCHAR  |        | NOT NULL, UNIQUE       |

### Tabla: usuarios
| Campo     | Tipo     | Clave  | Restricciones                        |
|-----------|----------|--------|--------------------------------------|
| id_user   | INTEGER  | PK     | NOT NULL, AUTO_INCREMENT             |
| nombre    | VARCHAR  |        | NOT NULL                             |
| email     | VARCHAR  |        | NOT NULL, UNIQUE                     |
| password  | VARCHAR  |        | NOT NULL                             |
| id_rol    | INTEGER  | FK     | NOT NULL, REFERENCES roles(id_rol)   |
