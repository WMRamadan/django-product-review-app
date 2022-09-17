from unicodedata import category
from django.test import TestCase
from products.models import Category, Product


class ProductsTest(TestCase):

    def setUp(self):
        cat_obj = Category.objects.create(name='test_category')
        Product.objects.create(name='test_product', description='this is a test product', image='static/img/sample.jpg', category=cat_obj)

    def test_get_product(self):
        prod_obj = Product.objects.get(name='test_product')
        self.assertEqual(prod_obj.name, 'test_product')
