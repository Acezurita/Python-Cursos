import os
import unittest
from calculadora import Calculadora

class CalculadoraSumaTest(unittest.TestCase):
    
    def setUp(self): #Fixture: SE ejecuta antes de cada testeada
        print("Se ejecuta antes")
        self.calc = Calculadora("Datos.txt")
    
    def test_suma_with_integers_successfully(self):
       # if suma(3,4) == 7:
       #   return True       Logica basica del test con if.
       #calc = Calculadora("Datos.txt")
       # assert 4 == 5, “lo números son diferentes”  <--Muestra el mensaje si no se cumple
       resultado = self.calc.suma(3,4)
       self.assertEqual(resultado,7) #Hace lo mismo que el if, esta es la forma correcta de testear.
       
    def test_suma_with_strings_return_message(self):
        resultado = self.calc.suma("nope","nipo")
        self.assertIsInstance(resultado,str)
        self.assertEqual(resultado,"Solo se aceptan numeros")
    
    def test_suma_with_numbers_string(self):
        resultado = self.calc.suma("7","8")
        self.assertEqual(resultado,15)
    
    def tearDown(self) -> None: #Fixture: Se ejecuta al final de cada testeada
        file = os.getcwd() + "\Datos.txt"
        os.remove(file)
        print("Se ejecuta al final de cada metodo")