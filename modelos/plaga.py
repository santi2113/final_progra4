from modelos.producto_control import ProductoControl


class Plaga(ProductoControl):
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia
