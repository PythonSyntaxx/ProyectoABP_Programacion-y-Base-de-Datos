# Sistema de Gestión de Usuarios 
import re
roles = [
    {"id_rol": 1, "rol": "admin"},
    {"id_rol": 2, "rol": "estandar"}
]

usuarios = [
    {"id_user": 1, "nombre": "admin", "email": "admin@gmail.com", "password": "Admin1", "id_rol": 1},
    {"id_user": 2, "nombre": "estandar", "email": "estandar@gmail.com", "password": "abc123", "id_rol": 2}
]

id_user_counter = 2

def validar_contraseña(password):
    if len(password) < 6:
        return False
    if not re.search(r"[a-zA-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

def menu_principal():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE USUARIOS =====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        else: 
            print("Adios")
            break

def login():
    email = input("Email: ")
    password = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["password"] == password:
            rol_nombre = obtener_nombre_rol(usuario["id_rol"])
            print(f"Bienvenido {usuario['nombre']} ({rol_nombre})")
            mostrar_menu(usuario)
            return

    print(" Email o contraseña incorrectos.")

def obtener_nombre_rol(id_rol):
    for rol in roles:
        if rol["id_rol"] == id_rol:
            return rol["rol"]
    return "Desconocido"

def mostrar_menu(usuario):
    if obtener_nombre_rol(usuario["id_rol"]) == "admin":
        while True:
            print(" MENÚ ADMIN ")
            print("1. Ver usuarios")
            print("2. Registrar usuario")
            print("3. Modificar usuario")
            print("4. Eliminar usuario")
            print("5. Cerrar seción ")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                ver_usuarios()
            elif opcion == "2":
                registrar_usuario()
            elif opcion == "3":
                modificar_usuario()
            elif opcion == "4":
                eliminar_usuario()
            elif opcion == "5":
                break
            else:
                print("Opcion invalida")
    else:
        while True:
            print(" MENÚ USUARIO ")
            print("1. Ver mis datos")
            print("2. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                ver_mis_datos(usuario)
            elif opcion == "2":
                break
            else:
                print("Opcion invalida")

def ver_usuarios():
    print("Usuarios registrados:")
    for u in usuarios:
        print(f"ID: {u['id_user']} - Nombre: {u['nombre']} - Email: {u['email']} - Rol: {obtener_nombre_rol(u['id_rol'])}")

def registrar_usuario():
    global id_user_counter
    print(" Registrar Usuario ")
    nombre = input("Nombre: ")
    email = input("Email: ")

    for u in usuarios:
        if u["email"] == email:
            print(" El email ya está registrado.")
            return
    while True:
        password = input("Contraseña: ")
        if validar_contraseña(password):
            break
        else:        
                 print(" La contraseña debe tener al menos 6 caracteres, incluir letras y números.")


    print("Roles disponibles:")
    for rol in roles:
        print(f"{rol['id_rol']} - {rol['rol']}")

    id_rol = int(input("Elige el rol: "))

    usuarios.append({
        "id_user": id_user_counter,
        "nombre": nombre,
        "email": email,
        "password": password,
        "id_rol": id_rol
    })
    id_user_counter += 1
    print(" Usuario registrado correctamente.")

def modificar_usuario():
    email = input("Email del usuario a modificar: ")
    for usuario in usuarios:
        if usuario["email"] == email:
            nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener): ") or usuario["nombre"]
            nuevo_email = input("Nuevo email (dejar en blanco para mantener): ") or usuario["email"]
            nueva_password = input("Nueva contraseña (dejar en blanco para mantener): ") or usuario["password"]
            nuevo_rol = input("Nuevo rol (dejar en blanco para mantener): ")
            nuevo_rol = int(nuevo_rol) if nuevo_rol else usuario["id_rol"]

            usuario.update({
                "nombre": nuevo_nombre,
                "email": nuevo_email,
                "password": nueva_password,
                "id_rol": nuevo_rol
            })
            print(" Usuario modificado correctamente.")
            return

    print(" Usuario no encontrado.")

def eliminar_usuario():
    email = input("Email del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario["email"] == email:
            confirmar = input(f"¿Estás seguro que querés eliminar a {email}? (s/n): ").lower()
            if confirmar == "s":
                usuarios.remove(usuario)
                print(" Usuario eliminado.")
            else:
                print(" Eliminación cancelada.")
            return
    print(" Usuario no encontrado.")

def ver_mis_datos(usuario):
    print(" MIS DATOS ")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Email: {usuario['email']}")
    print(f"Rol: {obtener_nombre_rol(usuario['id_rol'])}")

# Ejecutar programa
menu_principal()
