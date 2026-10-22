
import unittest
from decimal import Decimal

from practica_carrito_funciones import calcular_subtotal


class TestCarrito(unittest.TestCase):

    def test_precio_entero(self):
        resultado = calcular_subtotal(Decimal("30"), 2)
        self.assertEqual(resultado, Decimal("60"))

    def test_precio_decimal(self):
        resultado = calcular_subtotal(Decimal("35.50"), 3)
        self.assertEqual(resultado, Decimal("106.50"))

    def test_precision_decimal(self):
        resultado = calcular_subtotal(Decimal("0.10"), 3)
        self.assertEqual(resultado, Decimal("0.30"))


if __name__ == "__main__":
    unittest.main()
