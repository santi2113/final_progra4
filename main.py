
from modelos.CRUD import ProductoCRUD

# Crear una instancia de ProductoCRUD
crud = ProductoCRUD()

antibiotico1 = crud.crear_antibiotico("L001","Antibiotico 1", "Tipo 1", 15000,  "2 veces al día", "15 días", )
antibiotico2 = crud.crear_antibiotico("L001","Antibiotico 2", "Tipo 2",  15000, "3 veces al día","10 días",)

plaga1 = crud.crear_plaga("PL001", "Plaga 1", "Frecuencia 1", 10999, "Periodo 1")
plaga2 = crud.crear_plaga("PL002", "Plaga 2", "Frecuencia 2", 11999, "Periodo 2")


fertilizante1 = crud.crear_fertilizante("F001", "Fertilizante 1", "Mensual", 10099,"2024-06-30")
fertilizante2 = crud.crear_fertilizante("F002", "Fertilizante 2", "año", 10099, "2023-07-30")


# Crear algunos Clientes
cliente1 = crud.crear_cliente(1, "Cliente 1", "Direccion 1", "123456789")
cliente2 = crud.crear_cliente(2, "Cliente 2", "Direccion 2", "987654321")



# Crear algunas Facturas
factura1 = crud.crear_factura(cliente1.id)
factura2 = crud.crear_factura(cliente2.id)

# Agregar productos a las facturas
productos_factura1 = [(antibiotico1, 2), (plaga1, 1)]
factura1.productos = productos_factura1
factura1.calcular_total()

productos_factura2 = [(fertilizante1, 3), (plaga2, 2)]
factura2.productos = productos_factura2
factura2.calcular_total()

# Imprimir información de las facturas
print("Factura 1:")
factura1.imprimir_factura()

print("Factura 2:")
factura2.imprimir_factura()

# Actualizar un cliente
crud.actualizar_cliente(cliente1.id, "Nuevo Nombre", "Nueva Direccion", "987654321")

# Eliminar un fertilizante
crud.eliminar_fertilizante("F001")

# Eliminar una factura
crud.eliminar_factura(factura2.id)
