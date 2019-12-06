import unittest
from acme import Product
from acme_report import *


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        

    def test_stealability(self):
        self.assertEqual(Product('literally any name whatsoever').stealability()
                        ,'Kinda stealable.'
                        )

    def test_explode(self):
        self.assertEqual(Product('literally any name whatsoever').explode()
                        ,'...boom!'
                        )
    
    
class AcmeReportTests(unittest.TestCase):
    '''
    literally anything
    '''
    
    def test_default_num_products(self):
        iterator = 30
        self.assertEqual(len(generate_products(iterator)), iterator)
    
    
    def test_legal_names(self):
        test_list = generate_products(30)
        
        self.assertIn(inventory_report(test_list)[1][0].split(' ')[0], ADJECTIVES)
        self.assertIn(inventory_report(test_list)[1][0].split(' ')[1], NOUNS)
    
    
    
    """
    
    `test_legal_names` which checks that the generated names for a
  default batch of products are all valid possible names to generate (adjective,
  space, noun, from the lists of possible words)
    
    """
    
    

if __name__ == '__main__':
    unittest.main()