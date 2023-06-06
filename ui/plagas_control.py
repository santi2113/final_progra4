from PyQt5.QtWidgets import QMainWindow

from modelos.plaga import Plaga
from ui.plagas import Ui_MainWindow


class PlagasWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comprar.clicked.connect(self.agregar_plagas)
        self.productoCRUD = ProductoCRUD

        self.plaga = Plaga("PL001", "Plaga 1", "Frecuencia 1", 10999, "Periodo 4")
        self.plaga1 = Plaga("PL002", "Plaga 2", "Frecuencia 2", 17999, "Periodo 7")
        self.plaga2 = Plaga("PL003", "Plaga 3", "Frecuencia 1", 19999, "Periodo 12")



    def agregar_plagas(self):
        cantidad1 = self.ui.recibe_cantidad.text()
        cantidad2 = self.ui.recibe_cantidad_2.text()
        cantidad3 = self.ui.recibe_cantidad_3.text()
        factura_id = self.ui.recibe_id_factura_plaga.text()
        factura_id = int(factura_id)

        if factura_id:
            factura_encontrada = self.productoCRUD.buscar_factura(factura_id)

            if factura_encontrada:
                productos = factura_encontrada.productos

                if cantidad1 != "0":
                    productos.append((self.plaga, cantidad1))

                if cantidad2 != "0":
                    productos.append((self.plaga1, cantidad2))

                if cantidad3 != "0":
                    productos.append((self.plaga2, cantidad3))

                factura_encontrada.productos = productos



            else:
                self.ui.label_17.setText("Factura no encontrada")
