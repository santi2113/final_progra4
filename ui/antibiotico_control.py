from PyQt5.QtWidgets import QMainWindow

from modelos.antibiotico import Antibiotico
from ui.antibiotico import Ui_MainWindow


class AntibioticoWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comprar.clicked.connect(self.agregar_antibiotico)
        self.productoCRUD = ProductoCRUD


        self.antibiotico0 = Antibiotico("L001", "Antibiotico 0", "Tipo 0", 15000, "2 veces al día", "15 días", )
        self.antibiotico1 = Antibiotico("L002", "Antibiotico 1", "Tipo 1", 17000, "3 veces al día", "10 días", )
        self.antibiotico2 = Antibiotico("L003", "Antibiotico 2", "Tipo 2", 11000, "1 vece al día", "5 días", )



    def agregar_antibiotico(self):
        cantidad1 = self.ui.recibe_cantidad.text()
        cantidad2 = self.ui.recibe_cantidad_2.text()
        cantidad3 = self.ui.recibe_cantidad_3.text()
        factura_id = self.ui.recibe_id_factura_antibiotico.text()
        factura_id = int(factura_id)

        if factura_id:
            factura_encontrada = self.productoCRUD.buscar_factura(factura_id)

            if factura_encontrada:
                productos = factura_encontrada.productos

                if cantidad1 != "0":
                    productos.append((self.antibiotico0, cantidad1))

                if cantidad2 != "0":
                    productos.append((self.antibiotico1, cantidad2))

                if cantidad3 != "0":
                    productos.append((self.antibiotico2, cantidad3))

                factura_encontrada.productos = productos



            else:
                self.ui.label_17.setText("Factura no encontrada")
