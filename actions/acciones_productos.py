import os
from menus.menu_productos import mostrar_menu_productos
from file_manager import FileManagerProducto, FileManagerCategoria

def ejecutar_menu_productos():
    fm_prod = FileManagerProducto()
    fm_cat = FileManagerCategoria()
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_productos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- LISTADO DE PRODUCTOS ---")
            productos = fm_prod.get_all()
            categorias = {c['id']: c['nombre'] for c in fm_cat.get_all()} # Para mostrar el nombre en vez del ID
            
            if not productos:
                print("El inventario está vacío.")
            else:
                print(f"{'ID':<4} | {'NOMBRE':<15} | {'PRECIO':<8} | {'STOCK':<6} | {'CATEGORÍA'}")
                print("-" * 60)
                for p in productos:
                    nom_cat = categorias.get(p['id_categoria'], "N/A")
                    print(f"{p['id']:<4} | {p['nombre']:<15} | ${p['precio']:<7} | {p['stock']:<6} | {nom_cat}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            print("\n--- REGISTRAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            stock = input("Stock inicial: ")
            
            # Mostrar categorías disponibles para que el usuario elija
            print("\nCategorías disponibles:")
            lista_cat = fm_cat.get_all()
            for c in lista_cat: print(f" {c['id']}. {c['nombre']}")
            
            id_cat = input("\nSeleccione el ID de la categoría: ")
            
            if nombre and precio.replace('.','',1).isdigit() and id_cat.isdigit():
                fm_prod.insert(nombre, float(precio), int(stock), int(id_cat))
                print("\n[!] Producto añadido al inventario.")
            else:
                print("\n[!] Error en los datos ingresados.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_prod = input("ID del producto a editar: ")
            if id_prod.isdigit():
                prods = {p['id']: p for p in fm_prod.get_all()}
                id_int = int(id_prod)
                if id_int in prods:
                    nuevo_p = input(f"Nuevo precio [{prods[id_int]['precio']}]: ") or prods[id_int]['precio']
                    nuevo_s = input(f"Nuevo stock [{prods[id_int]['stock']}]: ") or prods[id_int]['stock']
                    
                    fm_prod.update(id_int, prods[id_int]['nombre'], float(nuevo_p), int(nuevo_s), prods[id_int]['id_categoria'])
                    print("\n[!] Producto actualizado.")
                else:
                    print("\n[!] Producto no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_elim = input("ID del producto a eliminar: ")
            if id_elim.isdigit():
                if fm_prod.delete(int(id_elim)):
                    print("\n[!] Producto eliminado.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break