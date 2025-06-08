# Sistema de Gestión de Usuarios – Aporte personal

Este repositorio forma parte del trabajo colaborativo para el desarrollo de un sistema de gestión de usuarios en consola con Python.

## 🧩 Mi aporte

Desarrollé las funciones `ver_usuarios()` y `registrar_usuario()`, incluidas en el menú exclusivo para administradores.

### 🔹 ver_usuarios()
Muestra una lista con los usuarios registrados, desplegando:
- ID de usuario
- Nombre
- Email
- Rol (nombre del rol, no el ID)

Utiliza la función `obtener_nombre_rol()` para traducir el ID de rol a su nombre legible.

### 🔹 registrar_usuario()
Permite registrar un nuevo usuario, incluyendo:
- Ingreso de nombre, email y contraseña
- Validación de formato de contraseña (mínimo 6 caracteres, letras y números)
- Control para evitar registros duplicados por email
- Selección interactiva del rol
- Asignación de un ID incremental mediante `id_user_counter`

Estas funciones fueron pensadas para garantizar la integridad de los datos y facilitar su uso desde un entorno de consola.

## 👨‍💻 Lenguaje utilizado
- Python

## 🚩 Estado del proyecto
✅ Funcional y probado. 


