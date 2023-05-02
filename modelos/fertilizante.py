from modelos.producto_control import ProductoControl


class Fertilizante(ProductoControl):
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, fecha_ultima_aplicacion, valor):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
