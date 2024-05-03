from django.test import Client, TestCase
from .models import Product
from .model_settings import Constants
import json




class ProductTestCase(TestCase):
    def setUp(self):
        products = Product.objects.bulk_create(
            [
                Product(sku="ABC987",name="PRUEBA 1"),
                Product(sku="XYZ098",name="PRUEBA 2"),
            ]
        )
        

    def test_new_product(self):
        """Test creating a new product with defeault stock of 100 pieces"""
        print("Test creating a new product with defeault stock of 100 pieces")
        products_before_inserting = Product.objects.all().count()
        data_new_product = {"sku": "ABC123","name": "Agua Natural 2L"}
        c = Client()
        response = c.post("/api/v1/product",data_new_product,headers={"accept": "application/json"})
        product_after_inserting = Product.objects.all().count()
        stock_of_new_product = Product.objects.get(sku="ABC123").stock

        self.assertEqual(response.status_code, 201)
        self.assertEqual(products_before_inserting + 1, product_after_inserting)
        self.assertEqual(stock_of_new_product, Constants.DEFAULT_QUANTITY_ON_INSERT.value)
    
    def test_get_all_products(self):
        """Test retriving all the products"""
        print("Test retriving all the products")
        products_in_db = Product.objects.all().count()
        c = Client()
        response = c.get("/api/v1/product",headers={"accept": "application/json"})
        products_in_api = json.loads(response.content)

        self.assertEqual(products_in_db, len(products_in_api))






