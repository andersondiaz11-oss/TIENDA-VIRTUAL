import unittest
from decimal import Decimal

from practica_carrito_funciones import calcular_subtotal
from unittest.mock import patch
from practica_carrito_funciones import validar_precio, validar_cantidad

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


    def test_validar_precio(self):
        entradas = ["0", "-5", "abc", "35,50"]

        with patch("builtins.input", side_effect=entradas):
            resultado = validar_precio()

        self.assertEqual(resultado, Decimal("35.50"))
    
    def test_validar_cantidad(self):
        entradas = ["0", "-5", "abc", "2.5", "3"]

        with patch("builtins.input", side_effect=entradas):
            resultado = validar_cantidad()

        self.assertEqual(resultado, 3)


if __name__ == "__main__":
    unittest.main()
