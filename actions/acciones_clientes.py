import os
from menus.menu_clientes import mostrar_menu_clientes
from file_manager import FileManagerCliente

# --- FUNCIONES DE VALIDACIÓN (REUTILIZABLES) ---

def leer_texto_puro(mensaje):
    """Solicita texto y rechaza si contiene números."""
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

def leer_numero_puro(mensaje, obligatorio=True):
    """Solicita entrada y rechaza si contiene letras (para RUC, Teléfono, etc)."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            if obligatorio:
                print("[!] Error: Este dato es obligatorio.")
                continue
            return "" # Si no es obligatorio, permite vacío
        
        if valor.isdigit():
            return valor
        else:
            print("[!] Error: Ingrese solo números. No se permiten letras ni símbolos.")

def leer_id_valido(mensaje):
    """Valida específicamente que el ID sea un número entero para evitar caídas."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("[!] Error: El ID debe ser un número entero.")

# --- MENÚ PRINCIPAL ---

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
            # VALIDACIONES DE ENTRADA
            nombre = leer_texto_puro("Nombre: ")
            ruc = leer_numero_puro("RUC/Cédula: ")
            telefono = leer_numero_puro("Teléfono: ")
            
            fm.insert(nombre, ruc, telefono)
            print("\n[!] Cliente guardado exitosamente.")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            print("\n--- EDITAR CLIENTE ---")
            id_int = leer_id_valido("Ingrese el ID del cliente a editar: ")
            
            clientes_data = {c['id']: c for c in fm.get_all()}
            
            if id_int in clientes_data:
                actual = clientes_data[id_int]
                print(f"Editando a: {actual['nombre']}")
                
                # Para editar, validamos pero permitimos que si el usuario no escribe nada, no cambie el dato
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

                # Validación de RUC (sin letras)
                while True:
                    n_ruc = input(f"Nuevo RUC [{actual['ruc']}]: ").strip()
                    if not n_ruc:
                        nuevo_ruc = actual['ruc']
                        break
                    if n_ruc.isdigit():
                        nuevo_ruc = n_ruc
                        break
                    print("[!] Error: El RUC debe ser solo números.")

                # Validación de Teléfono (sin letras)
                while True:
                    n_tel = input(f"Nuevo Teléfono [{actual['telefono']}]: ").strip()
                    if not n_tel:
                        nuevo_tel = actual['telefono']
                        break
                    if n_tel.isdigit():
                        nuevo_tel = n_tel
                        break
                    print("[!] Error: El teléfono debe ser solo números.")
                
                fm.update(id_int, nuevo_nom, nuevo_ruc, nuevo_tel)
                print("\n[!] Cliente actualizado.")
            else:
                print("\n[!] No se encontró un cliente con ese ID.")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            print("\n--- ELIMINAR CLIENTE ---")
            id_del = leer_id_valido("Ingrese el ID del cliente a eliminar: ")
            
            confirmar = input(f"¿Está seguro de eliminar el ID {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                if fm.delete(id_del):
                    print("\n[!] Cliente eliminado.")
                else:
                    print("\n[!] El ID no existe.")
            input("Presione Enter para continuar...")

        elif opcion == "5":
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")