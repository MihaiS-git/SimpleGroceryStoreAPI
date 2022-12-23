import pytest
from assertpy import assert_that
from validators.json_validator import *
from random import randint, choice

"""Testing API's functionality"""


class TestAPIFunctionality:

    @pytest.fixture
    def cart_1_id(self):
        return create_a_cart().json()['cartId']

    @pytest.fixture
    def cart_2_id(self):
        return create_a_cart().json()['cartId']

    @pytest.fixture
    def product_1_id(self):
        i = choice([randint(0, 5), randint(7, 19)])
        return get_all_products().json()[i]["id"]

    @pytest.fixture
    def product_2_id(self):
        i = choice([randint(0, 5), randint(7, 19)])
        return get_all_products().json()[i]["id"]

    @pytest.fixture
    def item_1_id(self, cart_1_id):
        i = choice([randint(0, 5), randint(7, 19)])
        product_id = get_all_products().json()[i]["id"]
        r = add_product_to_cart(cart_1_id, product_id)
        return r.json()["itemId"]

    def test_status(self):
        response = get_status()
        assert_that(validate_status_json())
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['status']).is_equal_to('UP')

    def test_head_api(self):
        r = get_api_head()
        assert_that(r.status_code).is_equal_to(200)

    def test_get_all_products(self):
        response = get_all_products()
        assert_that(validate_all_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(20)

    def test_get_coffee_category_products(self):
        response = get_products_list_by_category('coffee')
        assert_that(validate_coffee_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(3)

    def test_get_fresh_produce_category_products(self):
        response = get_products_list_by_category('fresh-produce')
        assert_that(validate_fresh_produce_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(5)

    def test_get_meat_seafood_category_products(self):
        response = get_products_list_by_category('meat-seafood')
        assert_that(validate_meat_seafood_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(4)

    def test_get_candy_category_products(self):
        response = get_products_list_by_category('candy')
        assert_that(validate_candy_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(3)

    def test_get_dairy_category_products(self):
        response = get_products_list_by_category('dairy')
        assert_that(validate_dairy_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(4)

    def test_get_bread_bakery_category_products(self):
        response = get_products_list_by_category('bread-bakery')
        assert_that(validate_bread_bakery_products_json() is True)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(len(response.json())).is_equal_to(1)

    def test_get_a_product_by_id(self, product_1_id):
        response = get_a_product_by_id(product_1_id)
        assert_that(response.status_code).is_equal_to(200)

    def test_create_a_cart(self):
        response = create_a_cart()
        assert_that(validate_cart_json()).is_equal_to(True)
        assert_that(response.status_code).is_equal_to(201)

    def test_add_item_to_cart(self, cart_1_id, product_1_id):
        response = add_product_to_cart(cart_1_id, product_1_id, 3)
        assert_that(validate_add_item_to_cart_json(response)).is_equal_to(True)
        assert_that(response.status_code).is_equal_to(201)

    def test_get_cart_items(self, cart_1_id, product_1_id):
        add_product_to_cart(cart_1_id, product_1_id, 3)
        response = get_cart_items(cart_1_id)
        assert_that(validate_get_cart_items_json(response)).is_equal_to(True)
        assert_that(response.status_code).is_equal_to(200)

    def test_replace_item_in_cart(self, cart_1_id, item_1_id, product_2_id):
        response = replace_item_in_cart(cart_1_id, item_1_id, product_2_id, 2)
        assert_that(response.status_code).is_equal_to(204)

    def test_delete_item_in_cart(self, cart_1_id, item_1_id):
        response = delete_item_in_cart(cart_1_id, item_1_id)
        assert_that(response.status_code).is_equal_to(204)

    def test_register_api_client_new_credentials(self):
        response = register_api_client_new_credentials()
        assert_that(response.status_code).is_equal_to(201)

    def test_create_new_order(self, cart_1_id, product_1_id, product_2_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        add_product_to_cart(test_cart, product_2_id, 2)
        response = create_new_order_good_credentials(test_cart)
        assert_that(validate_create_new_order_json(response)).is_equal_to(True)
        assert_that(response.status_code).is_equal_to(201)

    def test_get_all_orders(self, cart_1_id, cart_2_id, product_1_id, product_2_id):
        test_cart_1 = cart_1_id
        test_cart_2 = cart_2_id
        add_product_to_cart(test_cart_1, product_1_id, 2)
        add_product_to_cart(test_cart_2, product_2_id, 3)
        create_new_order_good_credentials(test_cart_1)
        create_new_order_good_credentials(test_cart_2)
        response = get_all_orders_good_credentials()
        assert_that(response.status_code).is_equal_to(200)

    def test_update_order(self, cart_1_id, product_1_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        response = create_new_order_good_credentials(test_cart)
        order_id = response.json()["orderId"]
        comment = 'Urgent'
        r = update_order_good_credentials(order_id, comment)
        assert_that(r.status_code).is_equal_to(204)

    def test_get_a_single_order(self, cart_1_id, product_2_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_2_id, 2)
        response = create_new_order_good_credentials(test_cart)
        order_id = response.json()["orderId"]
        r = get_a_single_order_good_credentials(order_id)
        assert_that(validate_single_order_json(r)).is_equal_to(True)
        assert_that(r.status_code).is_equal_to(200)

    def test_delete_an_order(self, cart_1_id, product_1_id):
        test_cart_1 = cart_1_id
        add_product_to_cart(test_cart_1, product_1_id, 2)
        order = create_new_order_good_credentials(test_cart_1)
        order_id = order.json()["orderId"]
        r = delete_an_order_good_credentials(order_id)
        assert_that(r.status_code).is_equal_to(204)
