import os
from menus.menu_categorias import mostrar_menu_categorias
from file_manager import FileManagerCategoria

# --- FUNCIONES DE VALIDACIÓN (REUTILIZABLES) ---

def leer_texto_puro(mensaje):
    """Solicita texto y rechaza si contiene números o está vacío."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("[!] Error: El campo no puede estar vacío.")
            continue
        # Verificamos que ningún carácter sea un dígito
        if any(char.isdigit() for char in valor):
            print("[!] Error: No se permiten números. Ingrese solo letras para el nombre.")
        else:
            return valor

def leer_id_valido(mensaje):
    """Valida que el ID sea un número entero para evitar caídas del sistema."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("[!] Error: El ID debe contener solo números.")

# --- MÓDULO DE CATEGORÍAS ---

def ejecutar_menu_categorias():
    fm = FileManagerCategoria()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_categorias()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- LISTADO DE CATEGORÍAS ---")
            categorias = fm.get_all()
            if not categorias:
                print("No hay categorías registradas.")
            else:
                print(f"{'ID':<5} | {'NOMBRE'}")
                print("-" * 25)
                for c in categorias:
                    print(f"{c['id']:<5} | {c['nombre']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            print("\n--- REGISTRAR CATEGORÍA ---")
            # VALIDACIÓN: No permite números ni vacíos
            nombre = leer_texto_puro("Nombre de la categoría: ")
            
            fm.insert(nombre)
            print("\n[!] Categoría guardada con éxito.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR CATEGORÍA ---")
            # VALIDACIÓN: Solo números para el ID
            id_int = leer_id_valido("ID de la categoría a editar: ")
            
            categorias_data = {c['id']: c for c in fm.get_all()}
            
            if id_int in categorias_data:
                actual = categorias_data[id_int]
                print(f"Editando: {actual['nombre']}")
                print("(Presione Enter para mantener el nombre actual)")