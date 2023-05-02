class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.total += float(producto.valor) * cantidad

    def imprimir_factura(self):
        print(f"Cliente: {self.cliente.nombre}")
        print("Productos:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} x{cantidad}: ${producto.valor}")
        print(f"Total: ${self.total}")
