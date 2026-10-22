"""Catálogo demostrativo: reemplazar por datos reales validados."""

PRODUCTOS = {
    1: {"nombre": "Shampoo de ejemplo", "precio": 30.00},
    2: {"nombre": "Acondicionador de ejemplo", "precio": 25.00},
}


def mostrar_productos():
    print("\nCatálogo demostrativo (precios en S/):")
    for codigo, producto in PRODUCTOS.items():
        print(f"{codigo}. {producto['nombre']} - S/ {producto['precio']:.2f}")
