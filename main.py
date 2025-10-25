from cliente_manager import ClienteManager

def main():
    manager = ClienteManager()
    
    while True:
        print("\n=============================================")
        print(" SISTEMA DE GESTIÓN DE CLIENTES AXANET (Python)")
        print("=============================================")
        print("1. Crear nuevo cliente")
        print("2. Consultar/Ver cliente existente")
        print("3. Actualizar cliente recurrente (Agregar solicitud)")
        print("4. Listar todos los clientes")
        print("5. Eliminar cliente (Solo para demostración)")
        print("6. Salir")
        
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            nombre = input("Nombre del nuevo cliente: ")
            contacto = input("Email/Contacto: ")
            servicio = input("Descripción de la PRIMERA solicitud: ")
            manager.crear_cliente(nombre, contacto, servicio)
            
        elif opcion == '2':
            print("\n--- CONSULTAR CLIENTE ---")
            print("Clientes disponibles:", manager.listar_clientes())
            nombre = input("Nombre del cliente a consultar: ")
            manager.leer_cliente(nombre)
            
        elif opcion == '3':
            print("\n--- ACTUALIZAR CLIENTE RECURRENTE ---")
            print("Clientes disponibles:", manager.listar_clientes())
            nombre = input("Nombre del cliente a actualizar: ")
            solicitud = input("Descripción de la NUEVA solicitud: ")
            manager.actualizar_cliente(nombre, solicitud)

        elif opcion == '4':
            print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
            clientes = manager.listar_clientes()
            if clientes:
                for c in clientes:
                    print(f"- {c}")
            else:
                print("No hay clientes registrados.")
            print("---------------------------------------")

        elif opcion == '5':
            print("\n--- ELIMINAR CLIENTE ---")
            print("Clientes disponibles:", manager.listar_clientes())
            nombre = input("Nombre del cliente a ELIMINAR: ")
            manager.eliminar_cliente(nombre)
            
        elif opcion == '6':
            print("Saliendo del sistema. ¡Adiós!")
            break
            
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()