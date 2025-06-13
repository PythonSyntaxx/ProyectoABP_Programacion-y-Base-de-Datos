# sistema.py
from gestor_usuarios import GestorUsuarios
from datos import usuarios

class Sistema:
    def __init__(self):
        self.gestor = GestorUsuarios()

    def login(self):
        email = input("Email: ")
        password = input("Contraseña: ")

        for u in usuarios:
            if u["email"] == email and u["password"] == password:
                print(f"Bienvenido {u['nombre']} ({self.gestor.obtener_nombre_rol(u['id_rol'])})")
                self.mostrar_menu(u)
                return
        print("Email o contraseña incorrectos.")

    def mostrar_menu(self, usuario):
        if self.gestor.obtener_nombre_rol(usuario["id_rol"]) == "admin":
            while True:
                print("\n MENÚ ADMIN ")
                print("1. Ver usuarios")
                print("2. Registrar usuario")
                print("3. Modificar usuario")
                print("4. Eliminar usuario")
                print("5. Cerrar sesión")
                opcion = input("Elige una opción: ")

                if opcion == "1":
                    self.gestor.ver_usuarios()
                elif opcion == "2":
                    self.gestor.registrar_usuario()
                elif opcion == "3":
                    self.gestor.modificar_usuario()
                elif opcion == "4":
                    self.gestor.eliminar_usuario()
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida")
        else:
            while True:
                print("\n MENÚ USUARIO ")
                print("1. Ver mis datos")
                print("2. Salir")
                opcion = input("Elige una opción: ")

                if opcion == "1":
                    self.gestor.ver_mis_datos(usuario)
                elif opcion == "2":
                    break
                else:
                    print("Opción inválida")
