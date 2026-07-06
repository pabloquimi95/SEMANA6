
from modelos.producto import Producto

# La clase Bebida hereda de Producto
class Bebida(Producto):
    def __init__(self, nombre, precio, disponibilidad, tamano):
        # Llama al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, disponibilidad)
        # Atributo exclusivo de esta clase hija
        self.tamano = tamano

    # Sobrescritura de método (Polimorfismo)
    def mostrar_informacion(self):
        print("\n=== BEBIDA ===")
        # Reutiliza el método de la clase padre para mostrar los datos comunes
        super().mostrar_informacion()
        print(f"Tamaño/Volumen: {self.tamano}")