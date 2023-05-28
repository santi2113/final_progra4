import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from clientes_control import ClientesWindow
from control_factura import FacturaWindow
from menu import Ui_MainWindow
from cliente import Ui_Form
from modelos.CRUD import ProductoCRUD


# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_cliente.clicked.connect(self.open_clientes)
        self.ui.btn_factura.clicked.connect(self.open_facturas)
        self.productoCRUD = ProductoCRUD()

    def open_clientes(self):
        self.cliente_dialog = ClientesWindow(self.productoCRUD)
        self.cliente_dialog.show()

    def open_facturas(self):
        self.factura_dialog = FacturaWindow(self.productoCRUD)
        self.factura_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
