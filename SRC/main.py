from sistema import Sistema

if __name__ == "__main__":
    sistema = Sistema()

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE USUARIOS =====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            sistema.gestor.registrar_usuario()
        elif opcion == "2":
            sistema.login()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
