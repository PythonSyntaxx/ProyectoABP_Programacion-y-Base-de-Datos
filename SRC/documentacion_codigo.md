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

# ERIC MATIAS ASTRADA
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


---
## Kevin Astrada

**Clase Usuario – Archivo usuario.py**

Desarrollé la clase Usuario, que define la estructura de un usuario del sistema. Esta clase incluye los siguientes atributos:

- id_user: un identificador único para cada usuario.

- nombre: el nombre del usuario.

- email: la dirección de correo.

- password: la contraseña.

- id_rol: un número que indica qué tipo de rol tiene el usuario (admin o estándar).

Además, implementé el método mostrar_datos(rol_nombre), que permite mostrar la información del usuario de forma clara en consola, incluyendo el nombre del rol, que se recibe como parámetro.

Esta clase se utiliza en varias partes del sistema:

Cuando se registra un nuevo usuario (registrar_usuario()), se crea una instancia de esta clase.

Cuando un usuario estándar inicia sesión y quiere ver su información, también se usa esta clase para mostrar sus datos.

**Clase Rol – Archivo rol.py**

También trabajé en la clase Rol, que define la estructura básica de un rol dentro del sistema. Esta clase tiene dos atributos:

- id_rol: un número identificador del rol.

- nombre: el nombre del rol (por ejemplo, "admin" o "estándar").

---

# Axel Rodrigo Leonel Cortez

Documentación: main.py

Descripción general

Este archivo representa el punto de entrada principal del sistema de gestión de usuarios en consola. Sirve como interfaz de navegación para que el usuario pueda registrarse, iniciar sesión o salir del programa.
Funcionalidad principal

    Importación del sistema:

from sistema import Sistema

Se importa la clase Sistema desde un módulo externo (sistema.py), que contiene la lógica principal de autenticación y gestión.

Inicialización del sistema:

    sistema = Sistema()

    Se crea una instancia de la clase Sistema, la cual permite acceder a sus métodos y funcionalidades (como registro e inicio de sesión).

    Menú principal (bucle infinito):
    Se presenta un menú interactivo en consola con tres opciones:

        Registrarse:
        Llama al método registrar_usuario() a través del gestor interno del sistema (sistema.gestor), permitiendo crear una nueva cuenta de usuario.

        Iniciar sesión:
        Llama al método login() del objeto Sistema, iniciando el proceso de autenticación de un usuario existente.

        Salir del programa:
        Finaliza el bucle y muestra un mensaje de despedida.

        Validación de entrada:
        Si el usuario ingresa una opción no válida, se muestra un mensaje de error y se vuelve a mostrar el menú.

Ejemplo del flujo de ejecución

===== SISTEMA DE GESTIÓN DE USUARIOS =====
1. Registrarse
2. Iniciar sesión
3. Salir
Elige una opción:

Dependencias

    Este archivo depende del módulo externo sistema.py, que debe contener la definición de la clase Sistema y su lógica de negocio.

Documentación: datos.py

Descripción general

Este módulo contiene los datos base necesarios para el funcionamiento del sistema de gestión de usuarios. Define tanto los roles disponibles como un conjunto inicial de usuarios predefinidos, además de una variable auxiliar para llevar el control del ID de usuario.

Contenido del archivo
🔹 roles

roles = [
    {"id_rol": 1, "rol": "admin"},
    {"id_rol": 2, "rol": "estandar"}
]

    Es una lista de diccionarios que define los tipos de rol disponibles en el sistema.

    Cada rol tiene:

        id_rol: identificador numérico del rol.

        rol: nombre del rol (ej. "admin" o "estandar").

    Esta estructura permite asignar privilegios diferenciados según el tipo de usuario.

🔹 usuarios

usuarios = [
    {"id_user": 1, "nombre": "admin", "email": "admin@gmail.com", "password": "Admin1", "id_rol": 1},
    {"id_user": 2, "nombre": "estandar", "email": "estandar@gmail.com", "password": "abc123", "id_rol": 2}
]

    Lista de usuarios registrados inicialmente en el sistema.

    Cada usuario contiene:

        id_user: ID único de usuario.

        nombre: nombre del usuario.

        email: correo electrónico utilizado para iniciar sesión.

        password: contraseña (almacenada en texto plano para este ejercicio).

        id_rol: referencia al rol asignado (coincide con los IDs en roles).

✅ Estos datos sirven como usuarios de prueba o base para iniciar el sistema.
🔹 id_user_counter

id_user_counter = 2

    Variable que lleva el conteo del último ID de usuario asignado.

    Se incrementa al registrar nuevos usuarios, asegurando que cada uno tenga un id_user único y consecutivo.

Ejemplo de uso

Este archivo es normalmente importado por otros módulos, como sistema.py, para acceder a la base de datos simulada en memoria. No contiene funciones, solo datos compartidos.
