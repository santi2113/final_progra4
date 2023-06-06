import unittest
from Crud.CRUD import ProductoCRUD


class TestProductoCRUD(unittest.TestCase):
    def setUp(self):
        self.crud = ProductoCRUD()

    def test_crear_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.assertEqual(cliente.nombre, "Cliente 1")
        self.assertEqual(cliente.direccion, "Dirección 1")
        self.assertEqual(cliente.telefono, "123456789")
        self.assertIsNotNone(cliente.cliente_id)

    def test_crear_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.cliente_id)
        self.assertIsNotNone(factura)
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(factura.productos, [])
        self.assertIsNotNone(factura.factura_id)

    def test_actualizar_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.crud.actualizar_cliente(cliente.cliente_id, "Nuevo Nombre")
        self.assertEqual(cliente.nombre, "Nuevo Nombre")

    def test_actualizar_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.cliente_id)
        antibiotico = self.crud.crear_antibiotico("AB001", "Antibiotico 1", "Tipo 1", 15000, "2 veces al día","15 días")
        factura.agregar_producto(antibiotico, 1)  # Actualizar aquí con la cantidad deseada
        self.assertEqual(factura.productos, [(antibiotico, 1)])
        self.assertEqual(factura.total, 15000)

    def test_eliminar_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        self.assertTrue(self.crud.eliminar_cliente(cliente.cliente_id))
        self.assertIsNone(self.crud.buscar_cliente(cliente.cliente_id))

    def test_eliminar_factura(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura = self.crud.crear_factura(cliente.cliente_id)
        self.assertTrue(self.crud.eliminar_factura(factura.factura_id))
        self.assertIsNone(self.crud.buscar_factura(factura.factura_id))

    def test_eliminar_facturas_cliente(self):
        cliente = self.crud.crear_cliente(1, "Cliente 1", "Dirección 1", "123456789")
        factura1 = self.crud.crear_factura(cliente.cliente_id)
        factura2 = self.crud.crear_factura(cliente.cliente_id)
        self.crud.eliminar_facturas_cliente(cliente)
        self.assertEqual(len(cliente.facturas), 0)