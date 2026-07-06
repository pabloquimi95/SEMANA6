
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # Instanciar el servicio encargado de gestionar el menú
    mi_restaurante = Restaurante()

    # Crear objetos (Instanciación)
    platillo1 = Platillo("Seco de Pollo", 4.50, True, "Platillo Fuerte")
    platillo2 = Platillo("Ceviche Mixto 7 Mares", 7.00, True, "Entrada/Especialidad")
    bebida1 = Bebida("Jugo de Limon", 1.50, True, "Vasos Grandes")

    # Registrar los objetos en la lista del restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)

    # --- Prueba de Encapsulación ---
    print("--- Prueba de Modificación de Precios ---")
    platillo1.cambiar_precio(-2.50)  # Debería dar error
    platillo1.cambiar_precio(5.00)   # Debería cambiarlo bien

    # --- Prueba de Polimorfismo ---
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()