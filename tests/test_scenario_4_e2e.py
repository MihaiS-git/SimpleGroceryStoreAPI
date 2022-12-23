import pytest
from assertpy import assert_that
from validators.json_validator import *

"""Scenario 4: Testing an end to end scenario"""


class TestScenario4:

    def test_status(self):
        response = get_status()
        assert_that(response.status_code).is_equal_to(200)

    def test_end_to_end_scenario(self):
        cart = create_a_cart()
        cart_id = cart.json()['cartId']
        item_1 = add_product_to_cart(cart_id, '4646', 4)
        item_1_id = item_1.json()['itemId']
        get_cart_items(cart_id)
        modify_cart_items_quantity(cart_id, item_1_id, 2)
        replace_item_in_cart(cart_id, item_1_id, '4643', 3)
        add_product_to_cart(cart_id, '7395')
        delete_item_in_cart(cart_id, item_1_id)
        register_api_client_new_credentials()
        order_1 = create_new_order_good_credentials(cart_id)
        order_1_id = order_1.json()['orderId']
        get_all_orders_good_credentials()
        update_order_good_credentials(order_1_id, "Urgent")
        r = delete_an_order_good_credentials(order_1_id)
        assert_that(r.status_code).is_equal_to(204)
