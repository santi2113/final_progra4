class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0
        self.id = None

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(producto.precio * cantidad for producto, cantidad in self.productos)


    def imprimir_factura(self):
        print("Cliente:", self.cliente.nombre)
        print("Productos:")
        for producto, cantidad in self.productos:
            print("- Nombre:", producto.nombre)
            print("  Cantidad:", cantidad)
        print("Total:", self.total)

    def cantidad_total_productos(self):
        total = 0
        for producto, cantidad in self.productos:
            total += cantidad
        return total
