import unittest
from user import validationUser

class Test_Validation_name(unittest.TestCase):
    def test_validation_name_is_correct(self):
        nombre = "Adrian"
        nombre_validate = validationUser.validate_nombre(nombre)
        self.assertIsNotNone(nombre_validate)
        self.assertEqual(nombre_validate,nombre)
        
    def test_validation_name_is_blank_fail(self):
        nombre = ""
        with self.assertRaises(ValueError):
            validationUser.validate_nombre(nombre)
    
    def test_validation_name_format_wrong_fail(self):
        nombre = "Adri4n"
        with self.assertRaises(ValueError):
            validationUser.validate_nombre(nombre)
    
    def test_validation_name_lenght_greater_50_letters_fail(self):
        nombre = "Adrian"*50
        with self.assertRaises(ValueError):
            validationUser.validate_nombre(nombre)
    
class Test_Validation_username(unittest.TestCase):
    def test_validation_username_is_correct(self):
        username = "acez"
        username_validate = validationUser.validate_username(username)
        self.assertIsNotNone(username_validate)
        self.assertEqual(username_validate,username)
        
    def test_validation_username_is_blank_fail(self):
        username = ""
        with self.assertRaises(ValueError):
            validationUser.validate_username(username)
    
    def test_validation_username_lenght_less_4_letters_fail(self):
        username = "Ac"
        with self.assertRaises(ValueError):
            validationUser.validate_username(username)
    
    def test_validation_username_lenght_greater_30_letters_fail(self):
        username = "Adrian"*30
        with self.assertRaises(ValueError):
            validationUser.validate_username(username)
            
class Test_Validation_edad(unittest.TestCase):
    def test_validation_edad_is_correct(self):
        edad = 29
        edad_validate = validationUser.validate_edad(edad)
        self.assertIsNotNone(edad_validate)
        self.assertEqual(edad_validate,edad)
        
    def test_validation_edad_is_blank_fail(self):
        edad = 0
        with self.assertRaises(ValueError):
            validationUser.validate_edad(edad)
    
    def test_validation_username_edad_less_18_years_old_fail(self):
        edad = 15
        with self.assertRaises(ValueError):
            validationUser.validate_edad(edad)
    
    def test_validation_edad_is_not_integer_fail(self):
        edad = "23"
        with self.assertRaises(ValueError):
            validationUser.validate_username(edad)
            

    

        
