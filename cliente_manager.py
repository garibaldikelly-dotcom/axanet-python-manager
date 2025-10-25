import os
import json
from datetime import datetime

CLIENTES_DIR = "datos_clientes"

class ClienteManager:
    def __init__(self):
        # La tabla hash (diccionario) que asocia nombre -> ruta del archivo
        self.clientes = {}
        self.asegurar_directorio()
        self.cargar_clientes()

    def asegurar_directorio(self):
        """Asegura que el directorio de datos exista."""
        if not os.path.exists(CLIENTES_DIR):
            os.makedirs(CLIENTES_DIR)
            print(f"[INFO] Directorio {CLIENTES_DIR} creado.")

    def cargar_clientes(self):
        """Carga los clientes existentes al inicializar."""
        self.clientes = {}
        for filename in os.listdir(CLIENTES_DIR):
            if filename.endswith(".txt"):
                nombre = filename.replace(".txt", "")
                self.clientes[nombre] = os.path.join(CLIENTES_DIR, filename)
        # print(f"[INFO] Clientes cargados: {list(self.clientes.keys())}")

    def crear_cliente(self, nombre, contacto, servicio):
        """Genera un archivo para un nuevo cliente."""
        nombre_normalizado = nombre.replace(" ", "_")
        if nombre_normalizado in self.clientes:
            print(f"[ERROR] Cliente '{nombre}' ya existe. Usa la opción de actualizar.")
            return False

        filepath = os.path.join(CLIENTES_DIR, f"{nombre_normalizado}.txt")
        
        try:
            with open(filepath, 'w') as f:
                f.write(f"--- FICHA DE CLIENTE CREADA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                f.write(f"ID: {nombre}\n")
                f.write(f"Contacto: {contacto}\n\n")
                f.write(f"--- SOLICITUD INICIAL ---\n")
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d')}\n")
                f.write(f"Servicio: {servicio}\n")
                f.write(f"-------------------------\n")
            
            self.clientes[nombre_normalizado] = filepath
            print(f"[ACCIÓN: CREACIÓN] Archivo '{nombre}.txt' creado exitosamente.")
            return True
        except Exception as e:
            print(f"[ERROR] No se pudo crear el archivo: {e}")
            return False

    def leer_cliente(self, nombre):
        """Lee y muestra el contenido del archivo de un cliente."""
        nombre_normalizado = nombre.replace(" ", "_")
        filepath = self.clientes.get(nombre_normalizado)

        if not filepath or not os.path.exists(filepath):
            print(f"[ERROR] Cliente '{nombre}' no encontrado.")
            return None

        with open(filepath, 'r') as f:
            contenido = f.read()
        
        print(f"\n--- CONTENIDO DE: {nombre_normalizado}.txt ---")
        print(contenido.strip())
        print("---------------------------------------------")
        return contenido
        
    def actualizar_cliente(self, nombre, nueva_solicitud):
        """Agrega una nueva solicitud al archivo de un cliente recurrente (Modificación)."""
        nombre_normalizado = nombre.replace(" ", "_")
        filepath = self.clientes.get(nombre_normalizado)
        
        if not filepath or not os.path.exists(filepath):
            print(f"[ERROR] Cliente '{nombre}' no encontrado.")
            return False

        try:
            # Abrir en modo 'a' (append) para agregar contenido al final
            with open(filepath, 'a') as f:
                f.write(f"\n--- NUEVA SOLICITUD AGREGADA: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d')}\n")
                f.write(f"Servicio: {nueva_solicitud}\n")
                f.write(f"---------------------------------------------------\n")
            
            print(f"[ACCIÓN: ACTUALIZACIÓN] Solicitud agregada a '{nombre}.txt' exitosamente.")
            return True
        except Exception as e:
            print(f"[ERROR] No se pudo actualizar el archivo: {e}")
            return False

    def eliminar_cliente(self, nombre):
        """Elimina el archivo de un cliente."""
        nombre_normalizado = nombre.replace(" ", "_")
        filepath = self.clientes.get(nombre_normalizado)

        if not filepath or not os.path.exists(filepath):
            print(f"[ERROR] Cliente '{nombre}' no encontrado.")
            return False

        try:
            os.remove(filepath)
            del self.clientes[nombre_normalizado]
            print(f"[ACCIÓN: ELIMINACIÓN] Archivo '{nombre}.txt' eliminado.")
            return True
        except Exception as e:
            print(f"[ERROR] No se pudo eliminar el archivo: {e}")
            return False

    def listar_clientes(self):
        """Lista todos los clientes en la tabla hash."""
        return list(self.clientes.keys())