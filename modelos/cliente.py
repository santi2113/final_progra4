class Cliente:
    def __init__(self, cliente_id, nombre, direccion, telefono):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.facturas = []

    def __str__(self):
        return f"ID: {self.cliente_id}\nNombre: {self.nombre}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"