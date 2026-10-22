
def validar_precio():
    while True:
        try:
            precio = float(input("Precio: S/ "))
            if precio > 0:
                return precio
            print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: Ingresa un precio válido.")


def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            print("Error: La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: Ingresa un número entero.")


def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def mostrar_resumen(carrito):
    total_general = 0

    print("\n=== RESUMEN DE COMPRA ===")

    for producto in carrito:
        subtotal = calcular_subtotal(
            producto["precio"], producto["cantidad"]
        )
        total_general += subtotal

        print(f"{producto['nombre']} - "
              f"{producto['cantidad']} unidades - "
              f"S/ {subtotal:.2f}")

    print(f"\nTOTAL A PAGAR: S/ {total_general:.2f}")


def main():
    carrito = []
    print("=== MESSIER DIVINE ===")

    while True:
        nombre = input("Nombre del producto: ").strip()

        if nombre == "":
            print("Error: Ingresa un producto.")
            continue

        precio = validar_precio()
        cantidad = validar_cantidad()

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        carrito.append(producto)

        while True:
            continuar = input(
                "¿Agregar otro producto? (S/N): "
            ).strip().upper()

            if continuar in ("S", "N"):
                break

            print("Error: Solo puedes ingresar S o N.")

        if continuar == "N":
            break

    mostrar_resumen(carrito)


if __name__ == "__main__":
    main()
