# Sistema de Gestión de Restaurante (Semana 6)

Este proyecto es una aplicación modular en Python que simula la gestión básica de un restaurante,
aplicando los principios de la **Programación Orientada a Objetos (POO)**.

El sistema permite registrar productos (platillos y bebidas), gestionar precios mediante
encapsulación y mostrar el menú usando polimorfismo.

---

## 📌 Características

- Registro de **Platillos** y **Bebidas**
- Uso de **Herencia** (Producto → Platillo / Bebida)
- Uso de **Encapsulación** (precio protegido)
- Uso de **Polimorfismo** (mostrar información dinámica)
- Organización del código en **paquetes y módulos**

---

## 🗂️ Estructura del Proyecto
restaurante_app/
│
├── modelos/
│ ├── producto.py
│ ├── platillo.py
│ ├── bebida.py
│ └── init.py
│
├── servicios/
│ ├── restaurante.py
│ └── init.py
│
├── main.py
└── README.md


---

## ▶️ Ejecución del Proyecto

Desde la carpeta `restaurante_app`, ejecutar:

```bash
py main.py