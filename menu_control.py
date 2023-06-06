import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Crud.CRUD import ProductoCRUD
from ui.antibiotico_control import AntibioticoWindow
from ui.clientes_control import ClientesWindow
from ui.control_factura import FacturaWindow
from ui.fertilizante_control import FertilizanteWindow
from ui.menu import Ui_MainWindow
from ui.plagas_control import PlagasWindow


# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_cliente.clicked.connect(self.open_clientes)
        self.ui.btn_factura.clicked.connect(self.open_facturas)
        self.ui.btn_plagas.clicked.connect(self.open_plagas)
        self.ui.pushButton_4.clicked.connect(self.open_ferlitizante)
        self.ui.pushButton_5.clicked.connect(self.open_antibiotico)
        self.productoCRUD = ProductoCRUD()

    def open_clientes(self):
        self.cliente_dialog = ClientesWindow(self.productoCRUD)
        self.cliente_dialog.show()

    def open_facturas(self):
        self.factura_dialog = FacturaWindow(self.productoCRUD)
        self.factura_dialog.show()

    def open_plagas(self):
        self.plaga_dialog = PlagasWindow(self.productoCRUD)
        self.plaga_dialog.show()

    def open_ferlitizante(self):
        self.fertilizante_dialog = FertilizanteWindow(self.productoCRUD)
        self.fertilizante_dialog.show()

    def open_antibiotico(self):
        self.antibiotico_dialog = AntibioticoWindow(self.productoCRUD)
        self.antibiotico_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

