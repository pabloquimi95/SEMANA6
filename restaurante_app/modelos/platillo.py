from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, disponibilidad, tipo_platillo):
        super().__init__(nombre, precio, disponibilidad)
        self.tipo_platillo = tipo_platillo

    def mostrar_informacion(self):
        print("\n=== PLATILLO ===")
        super().mostrar_informacion()
        print(f"Tipo de platillo: {self.tipo_platillo}")