from django.test import TestCase
from .models import Product

"""
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
"""
class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product(
            name='ttt',
            price=15000,
            description='ttt',
            stock=100
        )

        self.product.save()
    
    def test_create_product(self):
        first_product = Product.objects.all()
        self.assertEqual(first_product.count(), 1)