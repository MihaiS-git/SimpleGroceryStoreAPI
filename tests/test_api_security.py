import pytest
from assertpy import assert_that
from validators.json_validator import *
from random import randint, choice

"""Testing API's security"""


class TestAPISecurity:

    @pytest.fixture
    def cart_1_id(self):
        return create_a_cart().json()['cartId']

    @pytest.fixture
    def product_1_id(self):
        i = choice([randint(0, 5), randint(7, 19)])
        return get_all_products().json()[i]["id"]

    def test_register_api_client_new_credentials(self):
        pass

    def test_register_api_client_registered_name(self):
        r = register_api_client_registered_name()
        assert_that(r.status_code).is_equal_to(201)

    def test_register_api_client_registered_email(self):
        r = register_api_client_registered_email()
        assert_that(r.status_code).is_equal_to(409)

    def test_create_new_order_fake_token(self, cart_1_id, product_1_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        r = create_new_order_fake_credentials(test_cart)
        assert_that(validate_create_new_order_json(r)).is_equal_to(True)
        assert_that(r.status_code).is_equal_to(401)
        assert_that(r.json()['error']).is_equal_to("Invalid bearer token.")

    def test_get_all_orders_fake_token(self, cart_1_id, product_1_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        create_new_order_good_credentials(test_cart)
        r = get_all_orders_fake_credentials()
        print(r)
        assert_that(r.status_code).is_equal_to(401)
        assert_that(r.json()['error']).is_equal_to("Invalid bearer token.")

    def test_update_order_fake_token(self, cart_1_id, product_1_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        response = create_new_order_good_credentials(test_cart)
        order_id = response.json()["orderId"]
        comment = 'Urgent'
        r = update_order_fake_credentials(order_id, comment)
        assert_that(r.status_code).is_equal_to(401)
        assert_that(r.json()['error']).is_equal_to("Invalid bearer token.")

    def test_get_a_single_order_fake_token(self, cart_1_id, product_1_id):
        test_cart = cart_1_id
        add_product_to_cart(test_cart, product_1_id, 2)
        response = create_new_order_good_credentials(test_cart)
        order_id = response.json()["orderId"]
        r = get_a_single_order_fake_credentials(order_id)
        assert_that(r.status_code).is_equal_to(401)
        assert_that(r.json()['error']).is_equal_to("Invalid bearer token.")

    def test_delete_an_order_fake_token(self, cart_1_id, product_1_id):
        test_cart_1 = cart_1_id
        add_product_to_cart(test_cart_1, product_1_id, 2)
        order = create_new_order_good_credentials(test_cart_1)
        order_id = order.json()["orderId"]
        r = delete_an_order_fake_credentials(order_id)
        assert_that(r.status_code).is_equal_to(401)
        assert_that(r.json()['error']).is_equal_to("Invalid bearer token.")
