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
