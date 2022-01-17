import unittest
from user import User

class Test_User_name(unittest.TestCase):
    def test_create_user_name_succesfully(self):
        user =User("Adrian",29,"ACEZ")
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
    
    def test_create_user_name_is_blank_fail(self):
        with self.assertRaises(ValueError):
            user =User("",29,"ACEZ")
            user_saved = user.create()
            
    def test_create_user_name_is_alpha_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adri4n",29,"ACEZ")
            user_saved = user.create()
            
    def test_create_user_name_is_greater_than_50_letters_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adri4n"*50,29,"ACEZ")
            user_saved = user.create()  
            
class Test_User_username(unittest.TestCase):
    def test_create_user_username_succesfully(self):
        user =User("Adrian",29,"ACEZ")
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
    
    def test_create_user_username_is_blank_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian",29,"")
            user_saved = user.create()
            
    def test_create_user_name_is_lower_than_4_letters_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adri4n",29,"ACE")
            user_saved = user.create()
            
    def test_create_user_name_is_greater_than_30_letters_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian",29,"ACEZ"*30)
            user_saved = user.create()   
            
class Test_User_age(unittest.TestCase):
    def test_create_user_ege_succesfully(self):
        user =User("Adrian",29,"ACEZ")
        user_saved = user.create()
        self.assertIsNotNone(user_saved)
    
    def test_create_user_age_is_blank_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian",0,"ACEZ")
            user_saved = user.create()
            
    def test_create_user_age_is_not_integer_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian","29","ACEZ")
            user_saved = user.create()
            
    def test_create_user_age_is_lower_than_18_years_old_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian",17,"ACEZ")
            user_saved = user.create() 
    
    def test_create_user_age_is_lower_than_0_years_old_fail(self):
        with self.assertRaises(ValueError):
            user =User("Adrian",-30,"ACEZ")
            user_saved = user.create() 