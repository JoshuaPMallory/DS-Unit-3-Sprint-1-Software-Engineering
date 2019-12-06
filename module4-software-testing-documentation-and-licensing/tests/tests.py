import unittest
from sqrt import lazy_sqrt

class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square root functions!"""
    
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)
    
if __name__ == '__main__':
    unittest.main()
