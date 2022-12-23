import pytest
from assertpy import assert_that
from api_requests.api_requests import *

"""Scenario 2: Testing the unicity of all product's ids"""


class TestScenario2:

    def test_status(self):
        response = get_status()
        assert_that(response.status_code).is_equal_to(200)

    def test_coffee_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('coffee')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

    def test_fresh_produce_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('fresh-produce')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

    def test_meat_seafood_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('meat-seafood')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

    def test_candy_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('candy')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

    def test_dairy_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('dairy')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

    def test_bread_bakery_product_id_unicity(self):
        ids_list = []
        response = get_products_list_by_category('bread-bakery')
        products_list = response.json()
        for item in products_list:
            ids_list.append(item["id"])
        number_of_ids_in_list = len(ids_list)
        id_set = set(ids_list)
        number_of_ids_in_set = len(id_set)
        assert number_of_ids_in_list == number_of_ids_in_set, \
            f"Error: duplicate ids {number_of_ids_in_list} " \
            f"!= {number_of_ids_in_set}"

