import pytest
from assertpy import assert_that
from api_requests.api_requests import *

"""Scenario 3: Extended testing of the add products to cart functionality"""


class TestScenario3:

    @pytest.fixture
    def cart_1_id(self):
        return create_a_cart().json()['cartId']

    @pytest.fixture
    def products_list(self):
        return get_all_products().json()

    def test_status(self):
        response = get_status()
        assert_that(response.status_code, 200)

    def test_add_to_cart_all_unique_id_products_on_stock(self, cart_1_id, products_list):
        ids_list = []
        for item in products_list:
            if item['inStock'] and item['id'] not in ids_list:
                product_id = item['id']
                ids_list.append(product_id)
                product = get_a_product_by_id(product_id).json()
                stock_limit = product["current-stock"]
                r = add_product_to_cart(cart_1_id, product_id, stock_limit)
                assert_that(r.status_code).is_equal_to(201)
                assert_that(r.json()['created']).is_equal_to(True)

    def test_add_to_cart_all_products_on_stock(self, cart_1_id, products_list):
        for item in products_list:
            if item['inStock']:
                product_id = item['id']
                product = get_a_product_by_id(product_id).json()
                stock_limit = product["current-stock"]
                r = add_product_to_cart(cart_1_id, product_id, stock_limit)
                assert_that(r.status_code).is_equal_to(201)
                assert_that(r.json()['created']).is_equal_to(True)

    def test_add_to_cart_products_not_on_stock(self, cart_1_id, products_list):
        for item in products_list:
            if not item['inStock']:
                product_id = item['id']
                product = get_a_product_by_id(product_id).json()
                stock_limit = product["current-stock"]
                r = add_product_to_cart(cart_1_id, product_id, stock_limit)
                assert_that(r.status_code).is_equal_to(400)
                assert_that(r.json()['error']).is_equal_to("This product is not in stock and cannot be ordered.")
