import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from factura import Ui_MainWindow
from modelos.CRUD import ProductoCRUD

class FacturaWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_crear_factura.clicked.connect(self.crear_factura)
        self.ui.btn_buscar_factura.clicked.connect(self.buscar_factura)
        self.productoCRUD = ProductoCRUD

    def crear_factura(self):
        nombre_cliente = self.ui.recibe_nombre_cliente.text()
        if nombre_cliente:
            factura = self.productoCRUD.crear_factura(nombre_cliente)

            if nombre_cliente:
                self.ui.recibe_nombre_cliente.clear()
                self.ui.nombre_cliente.setText(factura.factura_id)
            else:
                self.ui.nombre_cliente.setText("Cliente no encontrado")

    def buscar_factura(self):
        factura_id = self.ui.recibe_id_factura.text()
        if factura_id:
            factura = self.productoCRUD.buscar_factura(factura_id)
            if factura_id:
                self.ui.mostrar_cliente_factura.setText(nombre_cliente)
                self.ui.mostrar_total_factura.setText(factura.total)
                self.ui.mostrar_productos_factura.setText(factura.productos)
            else:
                self.ui.mostrar_cliente_factura.setText("factura no encontrada")
                self.ui.mostrar_total_factura.setText("")
                self.ui.mostrar_productos_factura.setText("")









