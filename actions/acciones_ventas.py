import os
from datetime import datetime
from file_manager import FileManagerVenta, FileManagerCliente, FileManagerEmpleado, FileManagerProducto
from menus.menu_ventas import mostrar_menu_confirmacion_venta

def ejecutar_proceso_venta():
    fm_v = FileManagerVenta()
    fm_c = FileManagerCliente()
    fm_e = FileManagerEmpleado()
    fm_p = FileManagerProducto()

    os.system("cls" if os.name == "nt" else "clear")
    print(">>> REGISTRO DE NUEVA VENTA <<<")

    # 1. Seleccionar Cliente y Empleado (con validación para evitar errores de tipo)
    try:
        # Listar y seleccionar cliente
        clientes = fm_c.get_all()
        if not clientes:
            print("[!] No hay clientes registrados."); input(); return
        for c in clientes: print(f"[{c['id']}] {c['nombre']}")
        id_cli = int(input("\nID Cliente: "))
        
        # Listar y seleccionar empleado
        empleados = fm_e.get_all()
        if not empleados:
            print("[!] No hay empleados registrados."); input(); return
        for e in empleados: print(f"[{e['id']}] {e['nombre']}")
        id_emp = int(input("ID Vendedor: "))
    except ValueError:
        print("[!] Error: Los IDs deben ser números enteros."); input("Presione Enter para volver..."); return

    carrito = []
    total_venta = 0
    
    # 2. Agregar productos (Bucle con validación de "f" y "c")
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("--- PRODUCTOS DISPONIBLES ---")
        prods = fm_p.get_all()
        for p in prods: 
            print(f"ID: {p['id']} | {p['nombre']} | ${p['precio']} | Stock: {p['stock']}")
        
        print("\n" + "-"*30)
        print(f"ITEMS EN CARRITO: {len(carrito)} | TOTAL ACTUAL: ${total_venta}")
        print("-"*30)

        # Capturamos la entrada como texto para validar letras antes de convertir a número
        entrada = input("\nID Producto (f para finalizar / c para cancelar): ").strip().lower()
        
        if entrada == 'f': 
            break # Sale del bucle para ir a guardar
        if entrada == 'c': 
            print("\n[!] Proceso de venta cancelado."); input(); return

        # Intentamos convertir el ID a número solo si no es 'f' o 'c'
        try:
            cod_id = int(entrada)
        except ValueError:
            print(f"[!] '{entrada}' no es válido. Ingrese el ID numérico o 'f' para terminar.")
            input("Presione Enter..."); continue

        # Buscamos el producto en la lista
        prod_sel = next((p for p in prods if int(p['id']) == cod_id), None)
        
        if prod_sel:
            try:
                cant = int(input(f"Cantidad para {prod_sel['nombre']}: "))
                if cant <= 0:
                    print("[!] La cantidad debe ser mayor a 0."); input(); continue
                
                # Verificamos stock disponible
                if int(prod_sel['stock']) >= cant:
                    # AGREGAMOS AL CARRITO
                    carrito.append({
                        'id_producto': int(prod_sel['id']), 
                        'cantidad': cant, 
                        'precio_unitario': float(prod_sel['precio'])
                    })
                    total_venta += (float(prod_sel['precio']) * cant)
                    print(f"[✔] {prod_sel['nombre']} añadido."); input("Presione Enter para continuar...")
                else:
                    print(f"[!] Stock insuficiente. Disponible: {prod_sel['stock']}"); input()
            except ValueError:
                print("[!] Error: Ingrese un número entero para la cantidad."); input()
        else:
            print("[!] El ID de producto no existe."); input()

    # 3. Confirmación Final y GUARDADO REAL
    if carrito:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_confirmacion_venta(total_venta)
        op = input("Seleccione (1 para confirmar y guardar): ")
        
        if op == "1":
            # registrar_venta se encarga de: 
            # 1. Crear la venta en ventas.txt 
            # 2. Crear los detalles en detalle_ventas.txt
            # 3. Descontar el stock en productos.txt
            fm_v.registrar_venta(id_cli, id_emp, datetime.now().strftime("%Y-%m-%d %H:%M"), carrito)
            print("\n[✔] ¡VENTA REGISTRADA EXITOSAMENTE!"); input()
        else:
            print("\n[!] Venta no confirmada. Los datos no se guardaron."); input()
    else:
        print("\n[!] El carrito está vacío. Regresando al menú..."); input()