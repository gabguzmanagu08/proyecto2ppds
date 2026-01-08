import os
import sys

# Forzamos a Python a reconocer la carpeta actual para evitar errores de importación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones de los módulos de la tienda
from menus.menu_principal import mostrar_menu_principal
from actions.acciones_clientes import ejecutar_menu_clientes
from actions.acciones_empleados import ejecutar_menu_empleados
from actions.acciones_productos import ejecutar_menu_productos
from actions.acciones_categorias import ejecutar_menu_categorias
from actions.acciones_ventas import ejecutar_proceso_venta
from actions.acciones_reportes import ejecutar_reporte_ventas

def main():
    while True:
        # Limpiar pantalla según el sistema operativo
        os.system("cls" if os.name == "nt" else "clear")
        
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Gestión de Clientes
            ejecutar_menu_clientes()
        elif opcion == "2":
            # Gestión de Empleados
            ejecutar_menu_empleados()
        elif opcion == "3":
            # Gestión de Categorías
            ejecutar_menu_categorias()
        elif opcion == "4":
            # Gestión de Productos (Inventario)
            ejecutar_menu_productos()
        elif opcion == "5":
            # Transacción: Registrar Venta (incluye detalle_venta)
            ejecutar_proceso_venta()
        elif opcion == "6":
            # Reportes de Ventas y Ganancias
            ejecutar_reporte_ventas()
        elif opcion == "7":
            print("\nSaliendo del SISTEMA DE TIENDA. ¡Buen trabajo hoy!")
            break
        else:
            print("\n[!] Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()