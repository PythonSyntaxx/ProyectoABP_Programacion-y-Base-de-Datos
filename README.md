Desarrollé las funciones validar_contraseña(), la estructura del menú_principal() y la inicialización de roles y usuarios por defecto, fundamentales para el funcionamiento y seguridad del sistema.

- validar_contraseña()
Valida que la contraseña ingresada cumpla con criterios mínimos de seguridad:

Al menos 6 caracteres

Debe contener tanto letras como números

Esta función se utiliza durante el registro de usuarios y está diseñada para prevenir el uso de contraseñas débiles, asegurando un nivel básico de protección en el sistema.

- menú_principal()
Es el punto de entrada al sistema tras un login exitoso.
Muestra diferentes opciones según el rol del usuario (Administrador o Estándar), redirigiendo al conjunto de funciones permitidas para cada tipo.
Implementa una lógica clara de control de acceso basada en roles, manteniendo la usabilidad desde consola.

- Inicialización de roles y usuarios por defecto
Al inicio de la ejecución del programa, se precargan:

Una lista de roles definidos

Usuarios base con distintas configuraciones (nombre, email, contraseña y rol)
