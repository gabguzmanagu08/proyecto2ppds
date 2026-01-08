import os
from menus.menu_clientes import mostrar_menu_clientes
from file_manager import FileManagerCliente

def ejecutar_menu_clientes():
    fm = FileManagerCliente()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_clientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n" + "-"*40)
            print("       LISTADO DE CLIENTES")
            print("-"*40)
            clientes = fm.get_all()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                print(f"{'ID':<5} | {'NOMBRE':<20} | {'RUC/CED':<12} | {'TELÉFONO'}")
                print("-" * 55)
                for c in clientes:
                    print(f"{c['id']:<5} | {c['nombre']:<20} | {c['ruc']:<12} | {c['telefono']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO CLIENTE ---")
            nombre = input("Nombre: ")
            ruc = input("RUC/Cédula: ")
            telefono = input("Teléfono: ")
            
            if nombre and ruc:
                fm.insert(nombre, ruc, telefono)
                print("\n[!] Cliente guardado exitosamente.")
            else:
                print("\n[!] Error: El nombre y RUC son obligatorios.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR CLIENTE ---")
            id_buscado = input("Ingrese el ID del cliente a editar: ")
            if id_buscado.isdigit():
                # Buscamos si existe
                clientes = {c['id']: c for c in fm.get_all()}
                id_int = int(id_buscado)
                
                if id_int in clientes:
                    print(f"Editando a: {clientes[id_int]['nombre']}")
                    nuevo_nom = input("Nuevo Nombre (dejar vacío para mantener): ") or clientes[id_int]['nombre']
                    nuevo_ruc = input("Nuevo RUC (dejar vacío para mantener): ") or clientes[id_int]['ruc']
                    nuevo_tel = input("Nuevo Teléfono (dejar vacío para mantener): ") or clientes[id_int]['telefono']
                    
                    fm.update(id_int, nuevo_nom, nuevo_ruc, nuevo_tel)
                    print("\n[!] Cliente actualizado.")
                else:
                    print("\n[!] No se encontró un cliente con ese ID.")
            else:
                print("\n[!] ID inválido.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR CLIENTE ---")
            id_eliminar = input("Ingrese el ID del cliente a eliminar: ")
            if id_eliminar.isdigit():
                confirmar = input(f"¿Está seguro de eliminar el ID {id_eliminar}? (s/n): ")
                if confirmar.lower() == 's':
                    exito = fm.delete(int(id_eliminar))
                    if exito:
                        print("\n[!] Cliente eliminado.")
                    else:
                        print("\n[!] El ID no existe.")
            else:
                print("\n[!] ID inválido.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")