import os
from menus.menu_categorias import mostrar_menu_categorias
from file_manager import FileManagerCategoria

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
            nombre = input("Nombre de la categoría: ").strip()
            if nombre:
                fm.insert(nombre)
                print("\n[!] Categoría guardada.")
            else:
                print("\n[!] El nombre no puede estar vacío.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR CATEGORÍA ---")
            id_buscado = input("ID de la categoría a editar: ")
            if id_buscado.isdigit():
                categorias = {c['id']: c for c in fm.get_all()}
                id_int = int(id_buscado)
                if id_int in categorias:
                    nuevo_nom = input(f"Nuevo nombre [{categorias[id_int]['nombre']}]: ").strip()
                    if nuevo_nom:
                        # Debes tener el método 'update' en tu file_manager
                        fm.update(id_int, nuevo_nom)
                        print("\n[!] Categoría actualizada.")
                    else:
                        print("\n[!] Operación cancelada: nombre vacío.")
                else:
                    print("\n[!] ID no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR CATEGORÍA ---")
            id_eliminar = input("ID de la categoría a eliminar: ")
            if id_eliminar.isdigit():
                # Debes tener el método 'delete' en tu file_manager
                if fm.delete(int(id_eliminar)):
                    print("\n[!] Categoría eliminada.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break