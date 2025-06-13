# gestor_usuarios.py
import re
from datos import usuarios, roles, id_user_counter
from usuario import Usuario

class GestorUsuarios:
    def obtener_nombre_rol(self, id_rol):
        for rol in roles:
            if rol["id_rol"] == id_rol:
                return rol["rol"]
        return "Desconocido"

    def validar_contraseña(self, password):
        if len(password) < 6:
            return False
        if not re.search(r"[a-zA-Z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        return True

    def registrar_usuario(self):
        global id_user_counter
        nombre = input("Nombre: ")
        email = input("Email: ")

        for u in usuarios:
            if u["email"] == email:
                print("El email ya está registrado.")
                return

        while True:
            password = input("Contraseña: ")
            if self.validar_contraseña(password):
                break
            print("La contraseña debe tener al menos 6 caracteres, incluir letras y números.")

        print("Roles disponibles:")
        for rol in roles:
            print(f"{rol['id_rol']} - {rol['rol']}")

        id_rol = int(input("Elige el rol: "))

        nuevo_usuario = Usuario(id_user_counter, nombre, email, password, id_rol)
        usuarios.append(nuevo_usuario.__dict__)
        id_user_counter += 1
        print("Usuario registrado correctamente.")

    def ver_usuarios(self):
        for u in usuarios:
            print(f"ID: {u['id_user']} - Nombre: {u['nombre']} - Email: {u['email']} - Rol: {self.obtener_nombre_rol(u['id_rol'])}")

    def modificar_usuario(self):
        email = input("Email del usuario a modificar: ")
        for u in usuarios:
            if u["email"] == email:
                nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener): ") or u["nombre"]
                nuevo_email = input("Nuevo email (dejar en blanco para mantener): ") or u["email"]
                nueva_password = input("Nueva contraseña (dejar en blanco para mantener): ") or u["password"]
                nuevo_rol = input("Nuevo rol (dejar en blanco para mantener): ")
                nuevo_rol = int(nuevo_rol) if nuevo_rol else u["id_rol"]

                u.update({
                    "nombre": nuevo_nombre,
                    "email": nuevo_email,
                    "password": nueva_password,
                    "id_rol": nuevo_rol
                })
                print("Usuario modificado correctamente.")
                return
        print("Usuario no encontrado.")

    def eliminar_usuario(self):
        email = input("Email del usuario a eliminar: ")
        for u in usuarios:
            if u["email"] == email:
                confirmar = input(f"¿Estás seguro que querés eliminar a {email}? (s/n): ").lower()
                if confirmar == "s":
                    usuarios.remove(u)
                    print("Usuario eliminado.")
                else:
                    print("Eliminación cancelada.")
                return
        print("Usuario no encontrado.")

    def ver_mis_datos(self, usuario):
        usuario_obj = Usuario(**usuario)
        rol_nombre = self.obtener_nombre_rol(usuario["id_rol"])
        usuario_obj.mostrar_datos(rol_nombre)
