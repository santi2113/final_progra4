from PyQt5.QtWidgets import QMainWindow

from modelos.fertilizante import Fertilizante
from ui.fertilizante import Ui_MainWindow


class FertilizanteWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comprar.clicked.connect(self.agregar_fertilizante)
        self.productoCRUD = ProductoCRUD

        self.fertilizante = Fertilizante("F001", "Fertilizante ", "Mensual", 19999, "2024-06-30")
        self.fertilizante1 = Fertilizante("F002", "Fertilizante 1", "año", 10099, "2023-07-30")
        self.fertilizante2 = Fertilizante("F003", "Fertilizante 2", "año", 11099, "2025-09-24")



    def agregar_fertilizante(self):
        cantidad1 = self.ui.recibe_cantidad.text()
        cantidad2 = self.ui.recibe_cantidad_2.text()
        cantidad3 = self.ui.recibe_cantidad_3.text()
        factura_id = self.ui.recibe_id_factura_fertilizante.text()
        factura_id = int(factura_id)

        if factura_id:
            factura_encontrada = self.productoCRUD.buscar_factura(factura_id)

            if factura_encontrada:
                productos = factura_encontrada.productos

                if cantidad1 != "0":
                    productos.append((self.fertilizante, cantidad1))

                if cantidad2 != "0":
                    productos.append((self.fertilizante1, cantidad2))

                if cantidad3 != "0":
                    productos.append((self.fertilizante2, cantidad3))

                factura_encontrada.productos = productos



            else:
                self.ui.label_17.setText("Factura no encontrada")
