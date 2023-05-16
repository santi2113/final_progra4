import unittest
from modelos.CRUD import ProductoCRUD

class TestProductoCRUD(unittest.TestCase):
    def setUp(self):
        self.crud = ProductoCRUD()

    def test_crear_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.assertEqual(cliente.nombre, "Cliente 1")
        self.assertEqual(cliente.direccion, "Dirección 1")
        self.assertEqual(cliente.telefono, "123456789")
        self.assertIsNotNone(cliente.id)

    def test_crear_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.id)
        self.assertIsNotNone(factura)
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(factura.productos, [])
        self.assertIsNotNone(factura.id)

    def test_actualizar_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.crud.actualizar_cliente(cliente.id, "Nuevo Nombre", "Nueva Dirección", "987654321")
        self.assertEqual(cliente.nombre, "Nuevo Nombre")
        self.assertEqual(cliente.direccion, "Nueva Dirección")
        self.assertEqual(cliente.telefono, "987654321")

    def test_actualizar_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.telefono)
        antibiotico = self.crud.crear_antibiotico("AB001", "Antibiotico 1", "Tipo 1", 15000, "2 veces al día",
                                                  "15 días")
        factura.agregar_producto(antibiotico, 1)  # Actualizar aquí con la cantidad deseada
        self.assertEqual(factura.productos, [(antibiotico, 1)])
        self.assertEqual(factura.total, 15000)

    def test_eliminar_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.assertTrue(self.crud.eliminar_cliente(cliente.id))
        self.assertIsNone(self.crud.buscar_cliente(cliente.id))

    def test_eliminar_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.telefono)
        self.assertTrue(self.crud.eliminar_factura(factura.id))
        self.assertIsNone(self.crud.buscar_factura(factura.id))

    def test_eliminar_facturas_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura1 = self.crud.crear_factura(cliente.telefono)
        factura2 = self.crud.crear_factura(cliente.telefono)
        self.crud.eliminar_facturas_cliente(cliente)
        self.assertEqual
