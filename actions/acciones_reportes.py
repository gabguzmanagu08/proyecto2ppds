import os
from menus.menu_reportes import mostrar_menu_reportes
from file_manager import FileManagerVenta, FileManagerProducto, FileManagerCliente

def ejecutar_reporte_ventas():
    fm_v = FileManagerVenta()
    fm_p = FileManagerProducto()
    fm_c = FileManagerCliente()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_reportes()
        opcion = input("Seleccione una opción: ")

        ventas = fm_v.get_all_ventas()
        
        if opcion == "1": # Historial Detallado
            if not ventas:
                print("\nNo hay ventas registradas.")
            else:
                nombres_c = {c['id']: c['nombre'] for c in fm_c.get_all()}
                nombres_p = {p['id']: p['nombre'] for p in fm_p.get_all()}
                
                for v in ventas:
                    print(f"\nVENTA #{v['id']} | Cliente: {nombres_c.get(v['id_cliente'], 'N/A')} | Fecha: {v['fecha']}")
                    detalles = fm_v.get_detalles_por_venta(v['id'])
                    for d in detalles:
                        nom_prod = nombres_p.get(d['id_producto'], "Desconocido")
                        print(f"  - {nom_prod} x{d['cantidad']} | Subtotal: ${d['subtotal']}")
                    print(f"  TOTAL: ${v['total']}")
            input("\nPresione Enter para continuar...")

        elif opcion == "2": # Resumen Financiero
            total_acumulado = sum(float(v['total']) for v in ventas)
            print(f"\n" + "="*30)
            print(f" CANTIDAD DE VENTAS: {len(ventas)}")
            print(f" GANANCIA TOTAL:    ${total_acumulado:.2f}")
            print("="*30)
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            break