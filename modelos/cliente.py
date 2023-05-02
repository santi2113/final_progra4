class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def eliminar_factura(self, factura):
        self.facturas.remove(factura)

    def calcular_total_compras(self):
        total_compras = 0
        for factura in self.facturas:
            total_compras += factura.calcular_total()
        return total_compras
