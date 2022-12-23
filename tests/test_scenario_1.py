import pytest
from assertpy import assert_that
from api_requests.api_requests import *

"""Scenario 1: Testing client's acces to all products"""


class TestScenario1:

    def test_status(self):
        response = get_status()
        assert_that(response.status_code).is_equal_to(200)

    def test_product_type_number(self):
        all_products_list = get_all_products()
        all_products_number_by_type = len(all_products_list.json())

        coffee_list = get_products_list_by_category('coffee')
        coffee_products_by_type = len(coffee_list.json())
        fresh_produce_list = get_products_list_by_category('fresh-produce')
        fresh_produce_by_type = len(fresh_produce_list.json())
        meat_seafood_list = get_products_list_by_category('meat-seafood')
        meat_seafood_by_type = len(meat_seafood_list.json())
        candy_list = get_products_list_by_category('candy')
        candy_by_type = len(candy_list.json())
        dairy_list = get_products_list_by_category('dairy')
        dairy_by_type = len(dairy_list.json())
        bread_bakery_list = get_products_list_by_category('bread-bakery')
        bread_bakery_by_type = len(bread_bakery_list.json())

        product_type_sum_by_category = coffee_products_by_type \
                                       + fresh_produce_by_type \
                                       + meat_seafood_by_type \
                                       + candy_by_type + dairy_by_type \
                                       + bread_bakery_by_type

        assert all_products_number_by_type == product_type_sum_by_category, \
            f"Error: Number of product types error {all_products_number_by_type} " \
            f"!= {product_type_sum_by_category}"
