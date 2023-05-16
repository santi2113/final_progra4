from modelos.antibiotico import Antibiotico
from modelos.cliente import Cliente
from modelos.factura import Factura
from modelos.fertilizante import Fertilizante
from modelos.plaga import Plaga
import uuid


class ProductoCRUD:
    def __init__(self):
        self.antibioticos = []
        self.plagas = []
        self.fertilizantes = []
        self.clientes = []
        self.facturas = []
        self.productos = []

    def generar_id_factura():
        return str(uuid.uuid4())
    def crear_antibiotico(self, codigo, nombre, tipo, precio, dosis, duracion):
        antibiotico = Antibiotico(codigo, nombre, tipo, precio, dosis, duracion)
        self.antibioticos.append(antibiotico)
        return antibiotico

    def crear_plaga(self, codigo, nombre, frecuencia, precio, periodo):
        plaga = Plaga(codigo, nombre, frecuencia, precio, periodo)
        self.plagas.append(plaga)
        return plaga

    def crear_fertilizante(self, codigo, nombre, tipo_aplicacion, fecha_vencimiento, precio):
        fertilizante = Fertilizante(codigo, nombre, tipo_aplicacion, fecha_vencimiento, precio)
        self.fertilizantes.append(fertilizante)
        return fertilizante

    def crear_cliente(self, id, nombre, direccion, telefono):
        cliente = Cliente(id, nombre, direccion, telefono)
        self.clientes.append(cliente)
        return cliente

    def crear_factura(self, cliente_id):
        cliente = self.buscar_cliente(cliente_id)
        if cliente is None:
            return None

        factura = Factura(cliente)
        self.facturas.append(factura)
        return factura
    def buscar_antibiotico(self, codigo):
        for antibiotico in self.antibioticos:
            if antibiotico.codigo == codigo:
                return antibiotico
        return None

    def buscar_plaga(self, codigo):
        for plaga in self.plagas:
            if plaga.codigo == codigo:
                return plaga
        return None

    def buscar_fertilizante(self, codigo):
        for producto in self.fertilizantes:
            if isinstance(producto, Fertilizante) and producto.codigo == codigo:
                return producto
        return None


    def buscar_cliente(self, cliente_id):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def buscar_factura(self, factura_id):
        for factura in self.facturas:
            if factura.id == factura_id:
                return factura
        return None

    def actualizar_factura(self, factura_id, productos):
        factura = self.buscar_factura(factura_id)
        if factura is None:
            return False

        factura.productos = productos
        factura.calcular_total()
        return True

    def actualizar_cliente(self, cliente_telefono, nombre, direccion, telefono):
        cliente = self.buscar_cliente(cliente_telefono)
        if cliente is None:
            return False

        cliente.nombre = nombre
        cliente.direccion = direccion
        cliente.telefono = telefono
        return True

    def eliminar_fertilizante(self, codigo):
        fertilizante = self.buscar_fertilizante(codigo)
        if fertilizante:
            self.fertilizantes.remove(fertilizante)
            print("Fertilizante eliminado.")
        else:
            print("No se encontró el fertilizante con el código proporcionado.")
    def eliminar_cliente(self, cliente_id):
        cliente = self.buscar_cliente(cliente_id)
        if cliente is None:
            return False

        self.clientes.remove(cliente)
        self.eliminar_facturas_cliente(cliente)
        return True

    def eliminar_factura(self, factura_id):
        factura = self.buscar_factura(factura_id)
        if factura is None:
            return False

        self.facturas.remove(factura)
        return True

    def eliminar_facturas_cliente(self, cliente):
        facturas_cliente = [factura for factura in self.facturas if factura.cliente == cliente]
        self.facturas = [factura for factura in self.facturas if factura not in facturas_cliente]

