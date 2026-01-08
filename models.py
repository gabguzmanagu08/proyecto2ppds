# --- 1. CLIENTES ---
class Cliente:
    def __init__(self, id, nombre, ruc, telefono):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "ruc": ruc,
            "telefono": telefono
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        return f"{self.datos['id']}|{self.datos['nombre']}|{self.datos['ruc']}|{self.datos['telefono']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return Cliente(parts[0], parts[1], parts[2], parts[3])


# --- 2. EMPLEADOS ---
class Empleado:
    def __init__(self, id, nombre, cargo):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "cargo": cargo
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        return f"{self.datos['id']}|{self.datos['nombre']}|{self.datos['cargo']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return Empleado(parts[0], parts[1], parts[2])


# --- 3. CATEGORÍAS ---
class Categoria:
    def __init__(self, id, nombre):
        self.datos = {
            "id": int(id),
            "nombre": nombre
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        return f"{self.datos['id']}|{self.datos['nombre']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return Categoria(parts[0], parts[1])


# --- 4. PRODUCTOS ---
class Producto:
    def __init__(self, id, nombre, precio, stock, id_categoria):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "precio": float(precio),
            "stock": int(stock),
            "id_categoria": int(id_categoria)
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['precio']}|{d['stock']}|{d['id_categoria']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return Producto(parts[0], parts[1], parts[2], parts[3], parts[4])


# --- 5. VENTAS (Cabecera) ---
class Venta:
    def __init__(self, id, id_cliente, id_empleado, fecha, total):
        self.datos = {
            "id": int(id),
            "id_cliente": int(id_cliente),
            "id_empleado": int(id_empleado),
            "fecha": fecha,
            "total": float(total)
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_cliente']}|{d['id_empleado']}|{d['fecha']}|{d['total']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return Venta(parts[0], parts[1], parts[2], parts[3], parts[4])


# --- 6. DETALLE DE VENTA ---
class DetalleVenta:
    def __init__(self, id_venta, id_producto, cantidad, precio_unitario, subtotal):
        self.datos = {
            "id_venta": int(id_venta),
            "id_producto": int(id_producto),
            "cantidad": int(cantidad),
            "precio_unitario": float(precio_unitario),
            "subtotal": float(subtotal)
        }

    def __getitem__(self, key):
        return self.datos[key]

    def to_line(self):
        d = self.datos
        return f"{d['id_venta']}|{d['id_producto']}|{d['cantidad']}|{d['precio_unitario']}|{d['subtotal']}"

    @staticmethod
    def from_line(linea):
        parts = linea.strip().split("|")
        return DetalleVenta(parts[0], parts[1], parts[2], parts[3], parts[4])