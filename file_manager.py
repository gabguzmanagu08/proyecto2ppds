import os

# --- 1. CLIENTES ---
class FileManagerCliente:
    def __init__(self, filename="data/clientes.txt", counter_file="data/cont_clientes.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Cliente
        clientes = {}
        if not os.path.exists(self.filename): return clientes
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Cliente.from_line(line)
                    clientes[obj['id']] = obj
        return clientes

    def get_all(self):
        return [c for c in self._read_file().values()]

    def insert(self, nombre, ruc, telefono):
        from models import Cliente
        new_id = self._get_next_id()
        c = Cliente(new_id, nombre, ruc, telefono)
        with open(self.filename, "a") as f:
            f.write(c.to_line() + "\n")
        return c.datos
    def update(self, id_cliente, nombre, ruc, telefono):
        clientes = self._read_file()
        if id_cliente in clientes:
            # Actualizamos el objeto con los nuevos datos
            from models import Cliente
            clientes[id_cliente] = Cliente(id_cliente, nombre, ruc, telefono)
            self._write_file(clientes) # Debes tener un método que sobrescriba el archivo
            return True
        return False

    def delete(self, id_cliente):
        clientes = self._read_file()
        if id_cliente in clientes:
            del clientes[id_cliente]
            self._write_file(clientes)
            return True
        return False

    def _write_file(self, clientes):
        with open(self.filename, "w") as f:
            for c in clientes.values():
                f.write(c.to_line() + "\n")

# --- 2. EMPLEADOS ---
class FileManagerEmpleado:
    def __init__(self, filename="data/empleados.txt", counter_file="data/cont_empleados.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Empleado
        empleados = {}
        if not os.path.exists(self.filename): return empleados
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Empleado.from_line(line)
                    empleados[obj['id']] = obj
        return empleados

    def get_all(self):
        return [e for e in self._read_file().values()]

    def insert(self, nombre, cargo):
        from models import Empleado
        new_id = self._get_next_id()
        e = Empleado(new_id, nombre, cargo)
        with open(self.filename, "a") as f:
            f.write(e.to_line() + "\n")
        return e.datos
    
    def _write_file(self, empleados):
        with open(self.filename, "w") as f:
            for e in empleados.values():
                f.write(e.to_line() + "\n")

    def update(self, id_emp, nombre, cargo):
        empleados = self._read_file()
        if id_emp in empleados:
            from models import Empleado
            empleados[id_emp] = Empleado(id_emp, nombre, cargo)
            self._write_file(empleados)
            return True
        return False

    def delete(self, id_emp):
        empleados = self._read_file()
        if id_emp in empleados:
            del empleados[id_emp]
            self._write_file(empleados)
            return True
        return False

# --- 3. CATEGORIAS ---
class FileManagerCategoria:
    def __init__(self, filename="data/categorias.txt", counter_file="data/cont_categorias.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Categoria
        categorias = {}
        if not os.path.exists(self.filename): return categorias
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Categoria.from_line(line)
                    categorias[obj['id']] = obj
        return categorias

    def get_all(self):
        return [cat for cat in self._read_file().values()]

    def insert(self, nombre):
        from models import Categoria
        new_id = self._get_next_id()
        cat = Categoria(new_id, nombre)
        with open(self.filename, "a") as f:
            f.write(cat.to_line() + "\n")
        return cat.datos

    def _write_file(self, categorias):
        with open(self.filename, "w") as f:
            for c in categorias.values():
                f.write(c.to_line() + "\n")

    def update(self, id_cat, nombre):
        categorias = self._read_file()
        if id_cat in categorias:
            from models import Categoria
            categorias[id_cat] = Categoria(id_cat, nombre)
            self._write_file(categorias)
            return True
        return False

    def delete(self, id_cat):
        categorias = self._read_file()
        if id_cat in categorias:
            del categorias[id_cat]
            self._write_file(categorias)
            return True
        return False


# --- 4. PRODUCTOS ---
class FileManagerProducto:
    def __init__(self, filename="data/productos.txt", counter_file="data/cont_productos.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def _read_file(self):
        from models import Producto
        productos = {}
        if not os.path.exists(self.filename): return productos
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip():
                    obj = Producto.from_line(line)
                    productos[obj['id']] = obj
        return productos

    def get_all(self):
        return [p for p in self._read_file().values()]

    def _write_file(self, productos):
        with open(self.filename, "w") as f:
            for p in productos.values():
                f.write(p.to_line() + "\n")

    def insert(self, nombre, precio, stock, id_categoria):
        from models import Producto
        new_id = self._get_next_id()
        p = Producto(new_id, nombre, precio, stock, id_categoria)
        with open(self.filename, "a") as f:
            f.write(p.to_line() + "\n")
        return p.datos

    def actualizar_stock(self, id_producto, cantidad_vendida):
        productos = self._read_file()
        if id_producto in productos:
            productos[id_producto].datos['stock'] = int(productos[id_producto]['stock']) - cantidad_vendida
            self._write_file(productos)
            return True
        return False

    def update(self, id_prod, nombre, precio, stock, id_categoria):
        productos = self._read_file()
        if id_prod in productos:
            from models import Producto
            productos[id_prod] = Producto(id_prod, nombre, precio, stock, id_categoria)
            self._write_file(productos)
            return True
        return False

    def delete(self, id_prod):
        productos = self._read_file()
        if id_prod in productos:
            del productos[id_prod]
            self._write_file(productos)
            return True
        return False

# --- 5. VENTAS Y DETALLE VENTAS ---
class FileManagerVenta:
    def __init__(self, v_file="data/ventas.txt", d_file="data/detalle_ventas.txt", counter_file="data/cont_ventas.txt"):
        self.v_file = v_file
        self.d_file = d_file
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs("data", exist_ok=True)
        for f in [self.v_file, self.d_file]:
            if not os.path.exists(f):
                with open(f, "w") as arch: arch.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as arch: arch.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            current = int(f.read().strip() or 0)
        new_id = current + 1
        with open(self.counter_file, "w") as f:
            f.write(str(new_id))
        return new_id

    def registrar_venta(self, id_cliente, id_empleado, fecha, lista_items):
       
        from models import Venta, DetalleVenta
        fm_prod = FileManagerProducto()
        
        id_venta = self._get_next_id()
        total_venta = 0
        detalles_objetos = []

        # Procesar items y calcular total
        for item in lista_items:
            subtotal = item['cantidad'] * item['precio_unitario']
            total_venta += subtotal
            
            detalle = DetalleVenta(id_venta, item['id_producto'], item['cantidad'], item['precio_unitario'], subtotal)
            detalles_objetos.append(detalle)
            
            # Descontar stock
            fm_prod.actualizar_stock(item['id_producto'], item['cantidad'])

        # Guardar Cabecera Venta
        venta = Venta(id_venta, id_cliente, id_empleado, fecha, total_venta)
        with open(self.v_file, "a") as f:
            f.write(venta.to_line() + "\n")

        # Guardar Detalles
        with open(self.d_file, "a") as f:
            for d in detalles_objetos:
                f.write(d.to_line() + "\n")

        return venta.datos
    
    def get_all_ventas(self):
        from models import Venta
        ventas = []
        if not os.path.exists(self.v_file): return ventas
        with open(self.v_file, "r") as f:
            for line in f:
                if line.strip():
                    obj = Venta.from_line(line)
                    ventas.append(obj.datos)
        return ventas

    def get_detalles_por_venta(self, id_venta):
        from models import DetalleVenta
        detalles = []
        if not os.path.exists(self.d_file): return detalles
        with open(self.d_file, "r") as f:
            for line in f:
                if line.strip():
                    obj = DetalleVenta.from_line(line)
                    # CORRECCIÓN: Forzamos ambos a int para una comparación segura
                    if int(obj['id_venta']) == int(id_venta):
                        detalles.append(obj.datos)
        return detalles