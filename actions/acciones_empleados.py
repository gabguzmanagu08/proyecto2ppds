import os
from menus.menu_empleados import mostrar_menu_empleados
from file_manager import FileManagerEmpleado

def ejecutar_menu_empleados():
    fm = FileManagerEmpleado()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_empleados()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- LISTADO DE EMPLEADOS ---")
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
            print("\n--- REGISTRAR EMPLEADO ---")
            nombre = input("Nombre completo: ")
            cargo = input("Cargo (Vendedor, Administrador, etc.): ")
            
            if nombre and cargo:
                fm.insert(nombre, cargo)
                print("\n[!] Empleado registrado con éxito.")
            else:
                print("\n[!] Error: Todos los campos son obligatorios.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR EMPLEADO ---")
            id_buscado = input("ID del empleado a editar: ")
            if id_buscado.isdigit():
                empleados = {e['id']: e for e in fm.get_all()}
                id_int = int(id_buscado)
                if id_int in empleados:
                    nuevo_nom = input(f"Nuevo nombre [{empleados[id_int]['nombre']}]: ") or empleados[id_int]['nombre']
                    nuevo_cargo = input(f"Nuevo cargo [{empleados[id_int]['cargo']}]: ") or empleados[id_int]['cargo']
                    # Nota: Debes agregar el método 'update' en tu file_manager
                    fm.update(id_int, nuevo_nom, nuevo_cargo)
                    print("\n[!] Datos actualizados.")
                else:
                    print("\n[!] Empleado no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR EMPLEADO ---")
            id_eliminar = input("ID del empleado a eliminar: ")
            if id_eliminar.isdigit():
                # Nota: Debes agregar el método 'delete' en tu file_manager
                if fm.delete(int(id_eliminar)):
                    print("\n[!] Registro eliminado.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break