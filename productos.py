class Producto:

    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar(self, margen_de_venta):
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

    def imprimir(self):
        print("Id:", self.id)
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Costo:", self.costo)
        print("Cantidad:", self.cantidad)
        print("Precio de venta:", self.precio_de_venta)


productos = {}

producto1 = Producto(1, "Paleta", "Chocolate y frutos rojos", 5000, 1)
producto1.registrar(0.2)
productos[producto1.id] = producto1

producto2 = Producto(2, "Chococono", "Chocolate y vainilla", 3000, 2)
producto2.registrar(0.3)
productos[producto2.id] = producto2

# Imprime el listado de productos
for producto in productos.values():
    producto.imprimir()
