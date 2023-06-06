from PyQt5.QtWidgets import QMainWindow

from ui.factura import Ui_MainWindow


class FacturaWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_crear_factura.clicked.connect(self.crear_factura)
        self.ui.btn_buscar_factura.clicked.connect(self.buscar_factura)
        self.productoCRUD = ProductoCRUD

    def crear_factura(self):
        cliente_id = self.ui.recibe_nombre_cliente.text()
        if cliente_id:
            factura = self.productoCRUD.crear_factura(cliente_id)

            if cliente_id:
                self.ui.recibe_nombre_cliente.clear()
                self.ui.nombre_cliente.setNum((factura.factura_id))
            else:
                self.ui.nombre_cliente.setText("Cliente no encontrado")

    def buscar_factura(self):
        factura_id = self.ui.recibe_id_factura.text()
        factura_id = int(factura_id)
        if factura_id:
            factura_encontrada = self.productoCRUD.buscar_factura(factura_id)

            if factura_encontrada:
                total = factura_encontrada.calcular_total()
                self.ui.mostrar_cliente_factura.setText(factura_encontrada.cliente.cliente_id)
                self.ui.mostrar_total_factura.setText(str(total))
                self.ui.mostrar_productos_factura.setText(str(factura_encontrada.productos))
            else:
                self.ui.mostrar_cliente_factura.setText("Factura no encontrada")
                self.ui.mostrar_total_factura.setText("")
                self.ui.mostrar_productos_factura.setText("")










