Este archivo define la clase GestorUsuarios, que se encarga de gestionar todas las operaciones relacionadas con los usuarios dentro del sistema. Cada uno de los métodos implementados en esta clase corresponde a acciones que suelen figurar en un diagrama de clases, como registrar, ver, modificar y eliminar usuarios.

La clase utiliza una lista llamada usuarios y otra llamada roles, ambas importadas desde el archivo datos.py. Además, hace uso de la clase Usuario para representar a cada persona registrada.

Clase: GestorUsuarios obtener_nombre_rol(self, id_rol) Función: Busca y devuelve el nombre del rol (por ejemplo: "admin" o "estandar") según el ID que se le pase como parámetro.

Uso: Permite mostrar el rol del usuario de manera legible en lugar de solo el número.

validar_contraseña(self, password) Función: Comprueba si una contraseña es válida. La contraseña debe tener al menos 6 caracteres, incluir letras y números.

Importancia: Aumenta la seguridad de las cuentas creadas por los usuarios.

registrar_usuario(self) Función: Registra un nuevo usuario. Solicita nombre, email, contraseña y rol.

Detalles:

Evita duplicar usuarios con el mismo email.

Usa la clase Usuario para crear el nuevo usuario y lo convierte a diccionario para agregarlo a la lista usuarios.

Actualiza automáticamente el contador de IDs (id_user_counter).

ver_usuarios(self) Función: Muestra por pantalla todos los usuarios registrados.

Datos que muestra: ID, nombre, email y nombre del rol.

modificar_usuario(self) Función: Permite editar los datos de un usuario existente, buscándolo por email.

Comportamiento:

Si el campo queda vacío, mantiene el valor anterior.

Se puede cambiar nombre, email, contraseña y rol.

eliminar_usuario(self) Función: Elimina a un usuario del sistema según su email.

Detalles: Antes de borrar, pide una confirmación al usuario para evitar errores.

ver_mis_datos(self, usuario) Función: Muestra los datos personales del usuario actualmente logueado.

Cómo lo hace: Crea un objeto de la clase Usuario con los datos del diccionario recibido y llama al método mostrar_datos() de esa clase.

Esta clase cumple con su rol dentro del sistema al implementar todas las operaciones básicas necesarias para administrar usuarios. Se destaca el uso de programación orientada a objetos, la validación de datos y la integración con otras partes del sistema como la clase Usuario y el módulo datos.
