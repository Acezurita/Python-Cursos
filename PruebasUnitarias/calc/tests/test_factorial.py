import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
    
    def test_factorial_with_integers(self):
        resultado = factorial(5)
        self.assertEqual(resultado,120)
        
    def test_factorial_with_strings_raise_exception(self):
        with self.assertRaises(TypeError):
            factorial("Letrasss")