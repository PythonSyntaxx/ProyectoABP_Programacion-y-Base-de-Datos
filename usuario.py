# usuario.py

class Usuario:
    def __init__(self, id_user, nombre, email, password, id_rol):
        self.id_user = id_user
        self.nombre = nombre
        self.email = email
        self.password = password
        self.id_rol = id_rol

    def mostrar_datos(self, rol_nombre):
        print(" MIS DATOS ")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Rol: {rol_nombre}")
