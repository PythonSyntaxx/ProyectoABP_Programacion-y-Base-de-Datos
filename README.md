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
        print("\===== SISTEMA DE GESTIÓN DE USUARIOS =====")
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
