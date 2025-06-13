# Ariel Orlando Fernandez

# 📄 Documentación: `sistema.py`

## 📌 Descripción General

El módulo `sistema.py` actúa como la **interfaz principal del sistema de gestión de usuarios**, encargándose de manejar el **inicio de sesión (login)** y mostrar los menús correspondientes según el rol del usuario autenticado (admin o estándar). Se apoya en las clases importadas desde `gestor_usuarios` y los datos definidos en `datos.py`.

---

## 🧩 Dependencias

```python
from gestor_usuarios import GestorUsuarios
from datos import usuarios
```

- `GestorUsuarios`: clase que encapsula las operaciones CRUD sobre los usuarios.
- `usuarios`: estructura de datos que contiene los usuarios registrados.

---

## 🧱 Clase: `Sistema`

### 🔹 `__init__(self)`
Constructor de la clase. Instancia un objeto de `GestorUsuarios`.

### 🔹 `login(self)`
- Solicita email y contraseña.
- Verifica credenciales en la lista de usuarios.
- Si son correctas, da la bienvenida al usuario y accede al menú correspondiente.
- Si son incorrectas, muestra un mensaje de error.

### 🔹 `mostrar_menu(self, usuario)`
- Muestra un menú según el rol del usuario:
  - **Admin**:
    1. Ver usuarios
    2. Registrar usuario
    3. Modificar usuario
    4. Eliminar usuario
    5. Cerrar sesión
  - **Usuario estándar**:
    1. Ver mis datos
    2. Salir

Cada opción está asociada a métodos del objeto `GestorUsuarios`.

---

## ✅ Funcionalidades

| Función             | Rol            | Acción                                                                 |
|---------------------|----------------|------------------------------------------------------------------------|
| Login               | Todos          | Autenticación por email y contraseña                                   |
| Ver usuarios        | Admin          | Muestra todos los usuarios                                             |
| Registrar usuario   | Admin          | Permite añadir un nuevo usuario con rol                               |
| Modificar usuario   | Admin          | Permite actualizar los datos de un usuario existente                   |
| Eliminar usuario    | Admin          | Permite eliminar un usuario previa confirmación                        |
| Ver mis datos       | Estándar       | Muestra la información del usuario autenticado                         |

---

## 🔐 Consideraciones

- La validación de credenciales es básica y sin cifrado.
- No se almacena el estado de sesión más allá del usuario en memoria.
- Asume que los roles están predefinidos en la base de datos o archivo de datos.


Este archivo define la clase GestorUsuarios, que se encarga de gestionar todas las operaciones relacionadas con los usuarios dentro del sistema. Cada uno de los métodos implementados en esta clase corresponde a acciones que suelen figurar en un diagrama de clases, como registrar, ver, modificar y eliminar usuarios.

La clase utiliza una lista llamada usuarios y otra llamada roles, ambas importadas desde el archivo datos.py. Además, hace uso de la clase Usuario para representar a cada persona registrada.

 Clase: GestorUsuarios
 obtener_nombre_rol(self, id_rol)
Función: Busca y devuelve el nombre del rol (por ejemplo: "admin" o "estandar") según el ID que se le pase como parámetro.

Uso: Permite mostrar el rol del usuario de manera legible en lugar de solo el número.

 validar_contraseña(self, password)
Función: Comprueba si una contraseña es válida. La contraseña debe tener al menos 6 caracteres, incluir letras y números.

Importancia: Aumenta la seguridad de las cuentas creadas por los usuarios.

 registrar_usuario(self)
Función: Registra un nuevo usuario. Solicita nombre, email, contraseña y rol.

Detalles:

Evita duplicar usuarios con el mismo email.

Usa la clase Usuario para crear el nuevo usuario y lo convierte a diccionario para agregarlo a la lista usuarios.

Actualiza automáticamente el contador de IDs (id_user_counter).

 ver_usuarios(self)
Función: Muestra por pantalla todos los usuarios registrados.

Datos que muestra: ID, nombre, email y nombre del rol.

 modificar_usuario(self)
Función: Permite editar los datos de un usuario existente, buscándolo por email.

Comportamiento:

Si el campo queda vacío, mantiene el valor anterior.

Se puede cambiar nombre, email, contraseña y rol.

 eliminar_usuario(self)
Función: Elimina a un usuario del sistema según su email.

Detalles: Antes de borrar, pide una confirmación al usuario para evitar errores.

 ver_mis_datos(self, usuario)
Función: Muestra los datos personales del usuario actualmente logueado.

Cómo lo hace: Crea un objeto de la clase Usuario con los datos del diccionario recibido y llama al método mostrar_datos() de esa clase.


Esta clase cumple con su rol dentro del sistema al implementar todas las operaciones básicas necesarias para administrar usuarios. Se destaca el uso de programación orientada a objetos, la validación de datos y la integración con otras partes del sistema como la clase Usuario y el módulo datos.


