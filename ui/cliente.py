# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 564)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 30, 71, 31))
        self.label.setObjectName("label")
        self.recibe_numero_cedula = QtWidgets.QLineEdit(Form)
        self.recibe_numero_cedula.setGeometry(QtCore.QRect(210, 30, 311, 21))
        self.recibe_numero_cedula.setObjectName("recibe_numero_cedula")
        self.btn_crear_cliente = QtWidgets.QPushButton(Form)
        self.btn_crear_cliente.setGeometry(QtCore.QRect(570, 110, 75, 23))
        self.btn_crear_cliente.setObjectName("btn_crear_cliente")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.label_4.setObjectName("label_4")
        self.recibe_nombre_cliente = QtWidgets.QLineEdit(Form)
        self.recibe_nombre_cliente.setGeometry(QtCore.QRect(210, 80, 311, 21))
        self.recibe_nombre_cliente.setObjectName("recibe_nombre_cliente")
        self.recibe_direccion_cliente = QtWidgets.QLineEdit(Form)
        self.recibe_direccion_cliente.setGeometry(QtCore.QRect(210, 130, 311, 21))
        self.recibe_direccion_cliente.setObjectName("recibe_direccion_cliente")
        self.recibe_telefono_cliente = QtWidgets.QLineEdit(Form)
        self.recibe_telefono_cliente.setGeometry(QtCore.QRect(210, 170, 311, 21))
        self.recibe_telefono_cliente.setObjectName("recibe_telefono_cliente")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 81, 31))
        self.label_5.setObjectName("label_5")
        self.recibe_cedula_buscar = QtWidgets.QLineEdit(Form)
        self.recibe_cedula_buscar.setGeometry(QtCore.QRect(190, 260, 311, 21))
        self.recibe_cedula_buscar.setObjectName("recibe_cedula_buscar")
        self.btn_buscar_cliente = QtWidgets.QPushButton(Form)
        self.btn_buscar_cliente.setGeometry(QtCore.QRect(530, 260, 75, 23))
        self.btn_buscar_cliente.setObjectName("btn_buscar_cliente")
        self.btn_actualizar_cliente = QtWidgets.QPushButton(Form)
        self.btn_actualizar_cliente.setGeometry(QtCore.QRect(510, 360, 111, 23))
        self.btn_actualizar_cliente.setObjectName("btn_actualizar_cliente")
        self.btn_eliminar_cliente = QtWidgets.QPushButton(Form)
        self.btn_eliminar_cliente.setGeometry(QtCore.QRect(550, 500, 111, 23))
        self.btn_eliminar_cliente.setObjectName("btn_eliminar_cliente")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 320, 81, 31))
        self.label_6.setObjectName("label_6")
        self.recibe_cedula_actualizar = QtWidgets.QLineEdit(Form)
        self.recibe_cedula_actualizar.setGeometry(QtCore.QRect(170, 330, 311, 21))
        self.recibe_cedula_actualizar.setObjectName("recibe_cedula_actualizar")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(66, 392, 81, 21))
        self.label_7.setObjectName("label_7")
        self.recibe_nombre_cliente_actualizar = QtWidgets.QLineEdit(Form)
        self.recibe_nombre_cliente_actualizar.setGeometry(QtCore.QRect(160, 390, 311, 21))
        self.recibe_nombre_cliente_actualizar.setObjectName("recibe_nombre_cliente_actualizar")
        self.mostrar_cedula_cliente_buscar = QtWidgets.QLabel(Form)
        self.mostrar_cedula_cliente_buscar.setGeometry(QtCore.QRect(700, 250, 81, 20))
        self.mostrar_cedula_cliente_buscar.setObjectName("mostrar_cedula_cliente_buscar")
        self.mostrar_nombre_cliente_buscar = QtWidgets.QLabel(Form)
        self.mostrar_nombre_cliente_buscar.setGeometry(QtCore.QRect(700, 283, 81, 20))
        self.mostrar_nombre_cliente_buscar.setObjectName("mostrar_nombre_cliente_buscar")
        self.recibe_cedula_eliminar = QtWidgets.QLineEdit(Form)
        self.recibe_cedula_eliminar.setGeometry(QtCore.QRect(170, 500, 311, 21))
        self.recibe_cedula_eliminar.setObjectName("recibe_cedula_eliminar")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 490, 71, 31))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "cliente_id"))
        self.btn_crear_cliente.setText(_translate("Form", "crear cliente"))
        self.label_2.setText(_translate("Form", "nombre"))
        self.label_3.setText(_translate("Form", "direccion"))
        self.label_4.setText(_translate("Form", "telefono"))
        self.label_5.setText(_translate("Form", "numero_cliente"))
        self.btn_buscar_cliente.setText(_translate("Form", "buscar cliente"))
        self.btn_actualizar_cliente.setText(_translate("Form", "actualizar cliente"))
        self.btn_eliminar_cliente.setText(_translate("Form", "eliminar cliente"))
        self.label_6.setText(_translate("Form", "cliente id "))
        self.label_7.setText(_translate("Form", "nombre_nuevo"))
        self.mostrar_cedula_cliente_buscar.setText(_translate("Form", "TextLabel"))
        self.mostrar_nombre_cliente_buscar.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", "cliente_id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
