
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


