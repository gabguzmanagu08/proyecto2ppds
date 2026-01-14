import os
from menus.menu_productos import mostrar_menu_productos
from file_manager import FileManagerProducto, FileManagerCategoria

# --- FUNCIONES DE VALIDACIÓN (REUTILIZABLES) ---

def leer_texto_puro(mensaje):
    """Solicita texto y rechaza si contiene números o está vacío."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("[!] Error: El campo no puede estar vacío.")
            continue
        if any(char.isdigit() for char in valor):
            print("[!] Error: No se permiten números en este campo. Ingrese solo letras.")
        else:
            return valor

def leer_entero_puro(mensaje):
    """Solo permite números enteros (para Stock e IDs)."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("[!] Error: Ingrese un número entero válido.")

def leer_float_puro(mensaje):
    """Solo permite números decimales o enteros (para Precio)."""
    while True:
        valor = input(mensaje).strip()
        # Reemplazamos una coma por punto por si el usuario usa coma decimal
        valor = valor.replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            print("[!] Error: Ingrese un precio válido (ejemplo: 10.50).")

# --- MENÚ PRINCIPAL PRODUCTOS ---

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
            categorias = {c['id']: c['nombre'] for c in fm_cat.get_all()}
            
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
            nombre = leer_texto_puro("Nombre del producto: ")
            precio = leer_float_puro("Precio: ")
            stock = leer_entero_puro("Stock inicial: ")
            
            # Mostrar categorías para elegir
            print("\nCategorías disponibles:")
            lista_cat = fm_cat.get_all()
            if not lista_cat:
                print("[!] No hay categorías. Registre una primero.")
                input("Presione Enter...")
                continue
                
            for c in lista_cat: 
                print(f" {c['id']}. {c['nombre']}")
            
            id_cat = leer_entero_puro("\nSeleccione el ID de la categoría: ")
            
            fm_prod.insert(nombre, precio, stock, id_cat)
            print("\n[!] Producto añadido al inventario.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_int = leer_entero_puro("ID del producto a editar: ")
            
            prods = {p['id']: p for p in fm_prod.get_all()}
            if id_int in prods:
                actual = prods[id_int]
                print(f"Editando: {actual['nombre']}")
                print("(Presione Enter para mantener el valor actual)")

                # Validación de precio
                while True:
                    n_p = input(f"Nuevo precio [{actual['precio']}]: ").strip().replace(',', '.')
                    if not n_p:
                        nuevo_p = actual['precio']
                        break
                    try:
                        nuevo_p = float(n_p)
                        break
                    except ValueError:
                        print("[!] Error: Precio inválido.")

                # Validación de stock
                while True:
                    n_s = input(f"Nuevo stock [{actual['stock']}]: ").strip()
                    if not n_s:
                        nuevo_s = actual['stock']
                        break
                    if n_s.isdigit():
                        nuevo_s = int(n_s)
                        break
                    print("[!] Error: Stock debe ser un número.")
                
                fm_prod.update(id_int, actual['nombre'], nuevo_p, nuevo_s, actual['id_categoria'])
                print("\n[!] Producto actualizado.")
            else:
                print("\n[!] Producto no encontrado.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_elim = leer_entero_puro("ID del producto a eliminar: ")
            
            confirmar = input(f"¿Seguro que desea eliminar el producto {id_elim}? (s/n): ")
            if confirmar.lower() == 's':
                if fm_prod.delete(id_elim):
                    print("\n[!] Producto eliminado.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break