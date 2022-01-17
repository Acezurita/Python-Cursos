import unittest
from tests import test_calculadora 
from tests import test_factorial 

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity =2)
    
    suite.addTest(loader.loadTestsFromModule(test_calculadora))
    suite.addTest(loader.loadTestsFromModule(test_factorial))
    result = runner.run(suite)