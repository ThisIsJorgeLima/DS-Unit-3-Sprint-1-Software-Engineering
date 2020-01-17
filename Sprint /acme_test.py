import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_flammability(self):
        """Test default product price being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_explode(self):
        """Test explode method."""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):

    def test_generate_products(self):
        """Checking that default input to generate products is 30."""
        test = generate_products()
        self.assertTrue(len(test) == 30)
        
        