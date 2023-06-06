class ProductoControl:
    def __init__(self, registro_ICA, nombre, frecuencia_aplicacion, precio):
        self.registro_ICA = registro_ICA
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.precio = precio
    def __str__(self):
        return f"Registro ICA: {self.registro_ICA}\nNombre: {self.nombre}\nFrecuencia de aplicación: {self.frecuencia_aplicacion}\nPrecio: {self.precio}"