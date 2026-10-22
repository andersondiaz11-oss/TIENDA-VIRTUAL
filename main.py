"""Menú inicial del proyecto Messier Divine."""
from productos import PRODUCTOS, mostrar_productos
from ventas import calcular_total


def main():
    print("Bienvenido a Messier Divine (demostración)")
    while True:
        mostrar_productos()
        print("0. Salir")
        opcion = input("Selecciona un producto: ").strip()
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        try:
            codigo = int(opcion)
        except ValueError:
            print("Ingresa un código numérico válido.")
            continue
        if codigo not in PRODUCTOS:
            print("Producto no encontrado.")
            continue
        try:
            cantidad = int(input("Cantidad: ").strip())
            total = calcular_total(PRODUCTOS[codigo]["precio"], cantidad)
        except ValueError as error:
            print(f"Entrada incorrecta: {error}")
            continue
        print(f"Total: S/ {total:.2f}\n")


if __name__ == "__main__":
    main()
