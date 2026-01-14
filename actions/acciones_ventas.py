import os
from datetime import datetime
from file_manager import FileManagerVenta, FileManagerCliente, FileManagerEmpleado, FileManagerProducto
from menus.menu_ventas import mostrar_menu_confirmacion_venta

# --- FUNCIONES DE VALIDACIÓN (REUTILIZABLES) ---

def leer_id_valido(mensaje):
    """Valida que el ID sea un número entero para evitar caídas."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("[!] Error: El ID debe ser un número entero.")

def leer_entero_puro(mensaje):
    """Solo permite números enteros positivos para la cantidad."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else:
            print("[!] Error: Ingrese una cantidad válida (número entero mayor a 0).")

# --- MÓDULO DE PROCESO DE VENTA ---

def ejecutar_proceso_venta():
    fm_v = FileManagerVenta()
    fm_c = FileManagerCliente()
    fm_e = FileManagerEmpleado()
    fm_p = FileManagerProducto()

    os.system("cls" if os.name == "nt" else "clear")
    print(">>> REGISTRO DE NUEVA VENTA <<<")

    # 1. Seleccionar Cliente
    clientes = fm_c.get_all()
    if not clientes:
        print("[!] No hay clientes registrados."); input("Presione Enter..."); return
    
    print("\n--- CLIENTES ---")
    for c in clientes: print(f"[{c['id']}] {c['nombre']}")
    
    while True:
        id_cli = leer_id_valido("\nSeleccione ID Cliente: ")
        if any(c['id'] == id_cli for c in clientes): break
        print("[!] Error: El ID de cliente no existe.")

    # 2. Seleccionar Empleado
    empleados = fm_e.get_all()
    if not empleados:
        print("[!] No hay empleados registrados."); input("Presione Enter..."); return
    
    print("\n--- VENDEDORES ---")
    for e in empleados: print(f"[{e['id']}] {e['nombre']}")
    
    while True:
        id_emp = leer_id_valido("Seleccione ID Vendedor: ")
        if any(e['id'] == id_emp for e in empleados): break
        print("[!] Error: El ID de vendedor no existe.")

    carrito = []
    total_venta = 0.0
    
    # 3. Agregar productos al carrito
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"CLIENTE ID: {id_cli} | VENDEDOR ID: {id_emp}")
        print("-" * 40)
        print("--- PRODUCTOS DISPONIBLES ---")
        prods = fm_p.get_all()
        for p in prods: 
            print(f"ID: {p['id']} | {p['nombre']} | ${p['precio']} | Stock: {p['stock']}")
        
        print("\n" + "-"*40)
        print(f"ITEMS EN CARRITO: {len(carrito)} | TOTAL ACTUAL: ${total_venta:.2f}")
        print("-"*40)

        entrada = input("\nID Producto (f para finalizar / c para cancelar): ").strip().lower()
        
        if entrada == 'c': 
            print("\n[!] Venta cancelada."); input("Presione Enter..."); return
        if entrada == 'f': 
            break 

        # Validar si la entrada es un ID numérico
        if not entrada.isdigit():
            print(f"[!] '{entrada}' no es válido. Use el ID numérico o 'f'/'c'.")
            input("Continuar..."); continue

        cod_id = int(entrada)
        prod_sel = next((p for p in prods if p['id'] == cod_id), None)
        
        if prod_sel:
            cant = leer_entero_puro(f"Cantidad para {prod_sel['nombre']}: ")
            
            # Verificamos stock disponible
            if int(prod_sel['stock']) >= cant:
                # AGREGAMOS AL CARRITO
                carrito.append({
                    'id_producto': prod_sel['id'], 
                    'cantidad': cant, 
                    'precio_unitario': float(prod_sel['precio'])
                })
                total_venta += (float(prod_sel['precio']) * cant)
                print(f"[✔] {prod_sel['nombre']} añadido."); input("Siguiente...")
            else:
                print(f"[!] Stock insuficiente. Disponible: {prod_sel['stock']}"); input("Presione Enter...")
        else:
            print("[!] El ID de producto no existe."); input("Presione Enter...")

    # 4. Confirmación Final
    if carrito:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"RESUMEN DE VENTA")
        print(f"Total a pagar: ${total_venta:.2f}")
        mostrar_menu_confirmacion_venta(total_venta)
        
        op = input("Seleccione (1 para confirmar): ")
        if op == "1":
            # Guardado real en archivos
            fm_v.registrar_venta(id_cli, id_emp, datetime.now().strftime("%Y-%m-%d %H:%M"), carrito)
            print("\n[✔] ¡VENTA REGISTRADA EXITOSAMENTE EN SISTEMA!"); input("Presione Enter...")
        else:
            print("\n[!] Venta descartada."); input("Presione Enter...")
    else:
        print("\n[!] Carrito vacío."); input("Regresando...")