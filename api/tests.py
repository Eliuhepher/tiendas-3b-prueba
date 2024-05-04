import json
from django.test import Client, TestCase
from .models import Product
from .model_settings import Constants


class ProductTestCase(TestCase):
    """
    Class for testings API Methods
    """
    def setUp(self):
        Product.objects.bulk_create(
            [
                Product(sku="ABC987", name="PRUEBA 1"),
                Product(sku="XYZ098", name="PRUEBA 2"),
            ]
        )

    def test_new_product(self):
        """Test creating a new product with defeault stock of 100 pieces"""
        print("Test creating a new product with defeault stock of 100 pieces")
        products_before_inserting = Product.objects.all().count()
        data_new_product = {"sku": "ABC123", "name": "Agua Natural 2L"}
        c = Client()
        response = c.post(
            "/api/v1/product", data_new_product, headers={"accept": "application/json"}
        )
        product_after_inserting = Product.objects.all().count()
        stock_of_new_product = Product.objects.get(sku="ABC123").stock

        self.assertEqual(response.status_code, 201)
        self.assertEqual(products_before_inserting + 1, product_after_inserting)
        self.assertEqual(
            stock_of_new_product, Constants.DEFAULT_QUANTITY_ON_INSERT.value
        )

    def test_get_all_products(self):
        """Test retriving all the products"""
        print("Test retriving all the products")
        products_in_db = Product.objects.all().count()
        c = Client()
        response = c.get("/api/v1/product", headers={"accept": "application/json"})
        products_in_api = json.loads(response.content)

        self.assertEqual(products_in_db, len(products_in_api))

    def test_get_single_product(self):
        """Test get a single product"""
        print("Test get a single product")

        product_in_db = Product.objects.get(sku="ABC987").sku
        c = Client()
        response = c.get(
            f"/api/v1/product/{product_in_db}", headers={"accept": "application/json"}
        )
        products_in_api = json.loads(response.content)
        api_expected_response = {
            "sku": "ABC987",
            "name": "PRUEBA 1",
            "stock": 100,
        }

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(products_in_api, api_expected_response)

    def test_add_stock(self):
        """Test add 10 pieces to product's stock"""
        product = Product.objects.get(sku="XYZ098")
        initial_stock = product.stock
        data_stock_to_add = {"stock": 10}
        c = Client()
        response = c.patch(
            f"/api/v1/inventories/product/{product.sku}",
            data=json.dumps(data_stock_to_add),
            headers={"accept": "application/json", "content-type": "application/json"}
        )

        products_in_api = json.loads(response.content)
        final_stock = products_in_api["stock"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_stock, initial_stock + 10)

    def test_buy_products(self):
        """Test but products"""

        products_to_buy = [
            {"sku": "ABC987", "quantity": 1},
            {"sku": "XYZ098", "quantity": 1},
        ]

        initial_stock_product_1 = Product.objects.get(sku="ABC987").stock
        initial_stock_product_2 = Product.objects.get(sku="XYZ098").stock

        c = Client()
        response = c.post(
            "/api/v1/product/order",
            data=json.dumps(products_to_buy),
            content_type="application/json",
            headers={"accept": "application/json", "content-type": "application/json"}
        )

        final_stock_product_1 = Product.objects.get(sku="ABC987").stock
        final_stock_product_2 = Product.objects.get(sku="XYZ098").stock

        self.assertEqual(response.status_code, 200)
        self.assertEqual(final_stock_product_1, initial_stock_product_1 - 1)
        self.assertEqual(final_stock_product_2, initial_stock_product_2 - 1)
