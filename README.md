Sistema de Gestión de Usuarios – Contribución personal

Este repositorio corresponde a un proyecto colaborativo destinado al desarrollo de un sistema en consola para la gestión de usuarios, utilizando Python.
🧩 Mi contribución

Me encargué del desarrollo de las funciones login(), mostrar_menu(), obtener_nombre_rol().

def login()

Esta función gestiona el inicio de sesión del usuario.

    Pide al usuario su email y contraseña:

email = input("Email: ")
password = input("Contraseña: ")

Busca entre los usuarios registrados (usuarios) uno que coincida con el email y contraseña ingresados:

for usuario in usuarios:
    if usuario["email"] == email and usuario["password"] == password:

Si encuentra una coincidencia:

    Obtiene el nombre del rol del usuario (por ejemplo, "admin" o "usuario") usando obtener_nombre_rol.

    Muestra un mensaje de bienvenida.

    Llama a mostrar_menu(usuario) para mostrar el menú correspondiente.

    Finaliza la función con return.

Si no encuentra coincidencias, muestra un mensaje de error:

    print(" Email o contraseña incorrectos.")

🧾 def obtener_nombre_rol(id_rol)

Esta función recibe un id_rol (número o identificador del rol) y devuelve el nombre legible del rol, como "admin" o "usuario".

    Recorre la lista de roles (roles).

    Si encuentra un rol con el mismo id_rol, devuelve el nombre del rol:

    return rol["rol"]

    Si no lo encuentra, devuelve "Desconocido".

📋 def mostrar_menu(usuario)

Esta función muestra un menú diferente según el rol del usuario que inició sesión.
Si el rol del usuario es "admin":

Muestra el siguiente menú dentro de un bucle while True:

1. Ver usuarios
2. Registrar usuario
3. Modificar usuario
4. Eliminar usuario
5. Cerrar sesión

Y ejecuta la función correspondiente según la opción elegida.
Si el usuario no es admin:

Muestra un menú más sencillo:

1. Ver mis datos
2. Salir

Y también ejecuta la función correspondiente según la opción.
