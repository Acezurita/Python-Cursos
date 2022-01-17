import unittest
from tests import test_user
from tests import test_validations

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromModule(test_user))
suite.addTest(loader.loadTestsFromModule(test_validations))
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)