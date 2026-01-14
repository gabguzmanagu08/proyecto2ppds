import os
from menus.menu_empleados import mostrar_menu_empleados
from file_manager import FileManagerEmpleado

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
            print("[!] Error: No se permiten números en este campo. Ingrese solo letras.")
        else:
            return valor

def leer_id_valido(mensaje):
    """Valida que el ID sea un número entero para evitar caídas del sistema."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("[!] Error: El ID debe ser un número entero.")

# --- MENÚ PRINCIPAL EMPLEADOS ---

def ejecutar_menu_empleados():
    fm = FileManagerEmpleado()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_empleados()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n" + "-"*45)
            print("       LISTADO DE EMPLEADOS")
            print("-"*45)
            empleados = fm.get_all()
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print(f"{'ID':<5} | {'NOMBRE':<25} | {'CARGO'}")
                print("-" * 50)
                for e in empleados:
                    print(f"{e['id']:<5} | {e['nombre']:<25} | {e['cargo']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO EMPLEADO ---")
            # VALIDACIONES DE ENTRADA (Solo texto para nombre y cargo)
            nombre = leer_texto_puro("Nombre completo: ")
            cargo = leer_texto_puro("Cargo (Vendedor, Administrador, etc.): ")
            
            fm.insert(nombre, cargo)
            print("\n[!] Empleado registrado con éxito.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR EMPLEADO ---")
            id_int = leer_id_valido("Ingrese el ID del empleado a editar: ")
            
            empleados_data = {e['id']: e for e in fm.get_all()}
            
            if id_int in empleados_data:
                actual = empleados_data[id_int]
                print(f"Editando a: {actual['nombre']}")
                print("(Si desea mantener el dato actual, solo presione Enter)")
                
                # Validación de nombre (sin números)
                while True:
                    n_nom = input(f"Nuevo Nombre [{actual['nombre']}]: ").strip()
                    if not n_nom: 
                        nuevo_nom = actual['nombre']
                        break
                    if any(c.isdigit() for c in n_nom):
                        print("[!] Error: El nombre no puede tener números.")
                    else:
                        nuevo_nom = n_nom
                        break

                # Validación de cargo (sin números)
                while True:
                    n_car = input(f"Nuevo Cargo [{actual['cargo']}]: ").strip()
                    if not n_car:
                        nuevo_cargo = actual['cargo']
                        break
                    if any(c.isdigit() for c in n_car):
                        print("[!] Error: El cargo no puede tener números.")
                    else:
                        nuevo_cargo = n_car
                        break
                
                fm.update(id_int, nuevo_nom, nuevo_cargo)
                print("\n[!] Empleado actualizado.")
            else:
                print("\n[!] No se encontró un empleado con ese ID.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR EMPLEADO ---")
            id_del = leer_id_valido("Ingrese el ID del empleado a eliminar: ")
            
            confirmar = input(f"¿Está seguro de eliminar al empleado con ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                if fm.delete(id_del):
                    print("\n[!] Empleado eliminado correctamente.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")