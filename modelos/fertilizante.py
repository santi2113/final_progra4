from modelos.producto_control import ProductoControl


class Fertilizante(ProductoControl):
    def __init__(self, codigo, nombre, frecuencia_aplicacion, precio, fecha_ultima_aplicacion):
        super().__init__(codigo, nombre, frecuencia_aplicacion, precio)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
        self.codigo = codigo
