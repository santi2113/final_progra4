import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from cliente import Ui_Form
from modelos.CRUD import ProductoCRUD


class ClientesWindow(QMainWindow):
    def __init__(self, ProductoCRUD):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_crear_cliente.clicked.connect(self.crear_cliente)
        self.ui.btn_buscar_cliente.clicked.connect(self.buscar_cliente)
        self.ui.btn_actualizar_cliente.clicked.connect(self.actualizar_cliente)
        self.ui.btn_eliminar_cliente.clicked.connect(self.eliminar_cliente)
        self.productoCRUD = ProductoCRUD


    def crear_cliente(self):
        cliente_id = self.ui.recibe_numero_cedula.text()
        nombre = self.ui.recibe_nombre_cliente.text()
        direccion = self.ui.recibe_direccion_cliente.text()
        telefono = self.ui.recibe_telefono_cliente.text()
        if cliente_id and nombre and direccion and telefono:
            nombre_cliente = self.productoCRUD.crear_cliente(cliente_id, nombre, direccion, telefono)

            if nombre_cliente:
                self.ui.recibe_numero_cedula.clear()
                self.ui.recibe_nombre_cliente.clear()
                self.ui.recibe_direccion_cliente.clear()
                self.ui.recibe_telefono_cliente.clear()
        else:
            pass

    def buscar_cliente(self):
        cliente_id = self.ui.recibe_cedula_buscar.text()

        if cliente_id:
            cliente = self.productoCRUD.buscar_cliente(cliente_id)
            if cliente:
                self.ui.mostrar_cedula_cliente_buscar.setText(cliente.cliente_id)
                self.ui.mostrar_nombre_cliente_buscar.setText(cliente.nombre)
            else:
                self.ui.mostrar_cedula_cliente_buscar.setText("")
                self.ui.mostrar_nombre_cliente_buscar.setText("Cliente no encontrado")

    def actualizar_cliente(self):
        cliente_id = self.ui.recibe_cedula_actualizar.text()
        nombre = self.ui.recibe_nombre_cliente_actualizar.text()

        if cliente_id and nombre:
            self.productoCRUD.actualizar_cliente(cliente_id, nombre)
            self.ui.recibe_cedula_actualizar.clear()
            self.ui.recibe_nombre_cliente_actualizar.clear()

    def eliminar_cliente(self):
        cliente_id = self.ui.recibe_cedula_eliminar.text()

        if cliente_id:
            self.productoCRUD.eliminar_cliente(cliente_id)
            self.ui.recibe_cedula_eliminar.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clientesWindow = ClientesWindow()
    clientesWindow.show()
    sys.exit(app.exec_())
