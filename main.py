from modelos.antibiotico import Antibiotico
from modelos.cliente import Cliente
from modelos.factura import Factura
from modelos.fertilizante import Fertilizante
from modelos.plaga import Plaga

fertilizante1 = Fertilizante("1234", "Fertilizante ABC", "cada 15 días",  "2022-01-01", 15000)
fertilizante2 = Fertilizante("5678", "Fertilizante XYZ", "cada 30 días",  "2022-02-01" ,20000)


plaga1 = Plaga("9012", "Plaga ABC", "cada 15 días", 30000, 10)
plaga2 = Plaga("3456", "Plaga XYZ", "cada 30 días", 40000, 15)


antibiotico1 = Antibiotico(nombre="Antibiótico A", tipo="Bovinos", valor=10000, dosis=500, periodo_retiro="30 días")
antibiotico2 = Antibiotico(nombre="Antibiótico B", tipo="Porcinos", valor=8000, dosis=400, periodo_retiro="20 días")


factura1 = Factura([fertilizante1, plaga1])
factura2 = Factura([fertilizante2, antibiotico1, antibiotico2])


cliente1 = Cliente("Juan Perez", "Calle 1 # 2-3", "1234567")
cliente1.agregar_factura(factura1)

cliente2 = Cliente("Maria Gomez", "Carrera 4 # 5-6", "7654321")



# Crear facturas
factura1 = Factura(cliente=cliente1)
factura1.agregar_producto(fertilizante1, 2)
factura1.agregar_producto(antibiotico1, 1)

factura2 = Factura(cliente=cliente2)
factura2.agregar_producto(plaga1, 1)
factura2.agregar_producto(antibiotico2, 1)

# Imprimir información de la factura
print("Factura 1")
print(factura1)
print("Total: $", factura1.imprimir_factura())




# Crear un cliente con varias facturas
cliente3 = Cliente(nombre="Juan Pérez", direccion="calle 7", telefono="3188990843")
factura3 = Factura(cliente=cliente3)
factura3.agregar_producto(plaga1,1)
factura4 = Factura(cliente=cliente3)
factura4.agregar_producto(fertilizante1,3)
factura4.agregar_producto(antibiotico2,2)
factura5 = Factura(cliente=cliente3)
factura5.agregar_producto(antibiotico1,1)

# Imprimir información del cliente y sus facturas
print("Cliente 3")
print(cliente3)
print("Factura 3")
print(factura3)
print("Total: $", factura3.imprimir_factura())
print("Factura 4")
print(factura4)
print("Total: $", factura4.imprimir_factura())
print("Factura 5")
print(factura5)
print("Total: $", factura5.imprimir_factura())
