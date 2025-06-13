# rol.py

class Rol:
    def __init__(self, id_rol, nombre):
        self.id_rol = id_rol
        self.nombre = nombre

    def __str__(self):
        return f"{self.id_rol} - {self.nombre}"
