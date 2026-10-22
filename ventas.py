"""Funciones básicas de venta para practicar Python."""
from decimal import Decimal, ROUND_HALF_UP


def calcular_total(precio, cantidad):
    """Devuelve el total; rechaza cantidades no enteras o no positivas."""
    if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
        raise ValueError("La cantidad debe ser un número entero mayor que cero.")
    importe = Decimal(str(precio))
    if not importe.is_finite() or importe < 0:
        raise ValueError("El precio debe ser válido y no negativo.")
    return (importe * cantidad).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
