import unittest
from modelos.factura import Factura
from modelos.cliente import Cliente
from modelos.fertilizante import Fertilizante


class TestFactura(unittest.TestCase):
    def setUp(self):
        self.cliente1 = Cliente("Juan Perez", "Calle 1 # 2-3", "1234567")
        self.fertilizante1 = Fertilizante("1234", "Fertilizante ABC", "cada 15 días", "2022-01-01", 15000)
        self.factura1 = Factura(cliente=self.cliente1)

    def test_agregar_producto(self):
        # Verificar que la cantidad total de productos aumente correctamente
        self.assertEqual(self.factura1.cantidad_total_productos(), 0)
        self.factura1.agregar_producto(self.fertilizante1, 2)
        self.assertEqual(self.factura1.cantidad_total_productos(), 2)


        # Verificar que el precio total de la factura sea el correcto
        self.assertEqual(self.factura1.total, 30000)

if __name__ == '__main__':
    unittest.main()

