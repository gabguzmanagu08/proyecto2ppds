import os
from menus.menu_reportes import mostrar_menu_reportes
from file_manager import FileManagerVenta, FileManagerProducto, FileManagerCliente

# --- FUNCIONES DE VALIDACIÓN (REUTILIZABLES) ---

def leer_opcion_menu(mensaje, opciones_validas):
    """Valida que la opción del menú sea un número dentro del rango permitido."""
    while True:
        valor = input(mensaje).strip()
        if valor in opciones_validas:
            return valor
        else:
            print(f"[!] Error: Ingrese una opción válida ({', '.join(opciones_validas)}).")

# --- MÓDULO DE REPORTES ---

def ejecutar_reporte_ventas():
    fm_v = FileManagerVenta()
    fm_p = FileManagerProducto()
    fm_c = FileManagerCliente()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_reportes()
        
        # Validamos que solo ingrese opciones del 1 al 3
        opcion = leer_opcion_menu("Seleccione una opción: ", ["1", "2", "3"])

        ventas = fm_v.get_all_ventas()
        
        if opcion == "1": # Historial Detallado
            print("\n--- HISTORIAL DETALLADO DE VENTAS ---")
            if not ventas:
                print("\nNo hay ventas registradas.")
            else:
                # Diccionarios para búsqueda rápida (mapeo de nombres)
                nombres_c = {c['id']: c['nombre'] for c in fm_c.get_all()}
                nombres_p = {p['id']: p['nombre'] for p in fm_p.get_all()}
                
                for v in ventas:
                    print(f"\nVENTA #{v['id']} | Cliente: {nombres_c.get(v['id_cliente'], 'N/A')} | Fecha: {v['fecha']}")
                    detalles = fm_v.get_detalles_por_venta(v['id'])
                    
                    for d in detalles:
                        nom_prod = nombres_p.get(d['id_producto'], "Desconocido")
                        # Validamos que cantidad y subtotal se manejen como tipos correctos
                        cantidad = int(d['cantidad'])
                        subtotal = float(d['subtotal'])
                        print(f"  - {nom_prod} x{cantidad} | Subtotal: ${subtotal:.2f}")
                    
                    total_venta = float(v['total'])
                    print(f"  TOTAL VENTA: ${total_venta:.2f}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2": # Resumen Financiero
            print("\n--- RESUMEN FINANCIERO ---")
            if not ventas:
                print("\nNo hay datos suficientes para generar un resumen.")
            else:
                try:
                    # Forzamos la conversión a float para asegurar que no se sumen strings
                    total_acumulado = sum(float(v['total']) for v in ventas)
                    print(f"\n" + "="*35)
                    print(f" CANTIDAD DE VENTAS: {len(ventas)}")
                    print(f" GANANCIA TOTAL:     ${total_acumulado:.2f}")
                    print("="*35)
                except ValueError:
                    print("[!] Error crítico: Existen datos corruptos en el archivo de ventas.")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            # Salir al menú principal
            break