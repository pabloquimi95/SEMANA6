
class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        # Atributos públicos comunes para todos los productos
        self.nombre = nombre
        self.disponibilidad = disponibilidad
        # Atributo protegido mediante encapsulación (doble guion bajo)
        self.__precio = precio

    # Método público para obtener el precio de forma controlada
    def obtener_precio(self):
        return self.__precio

    # Método público para modificar el precio aplicando la validación de la rúbrica
    def cambiar_precio(self, nuevo_precio):
        # Validación: El precio no puede ser negativo ni igual a cero
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"Error: El precio de '{self.nombre}' debe ser mayor que cero.")

    # Método base que será redefinido en las clases hijas (Polimorfismo)
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Estado: {estado}")