
class Restaurante:
    def __init__(self):
        # Lista vacía para almacenar los objetos (Platillos y Bebidas)
        self.productos = []

    # Método para registrar un producto en la lista del menú
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método que demuestra polimorfismo al recorrer la lista
    def mostrar_menu(self):
        print("\n================ MENÚ DEL RESTAURANTE 7 MARES ================")
        if not self.productos:
            print("No hay productos registrados en el menú.")
            return

        # Recorre la lista de productos de forma dinámica
        for producto in self.productos:
            # Cada objeto responde según su propia clase (Polimorfismo)
            producto.mostrar_informacion()
        print("\n======================================================")