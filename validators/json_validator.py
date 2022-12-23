from api_requests.api_requests import *
import jsonschema
from jsonschema import validate


def validate_json_schema(json_data, json_schema):
    try:
        validate(instance=json_data, schema=json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def validate_status_json():
    status_schema = json.loads(open('../json_schema/status_schema.txt').read())
    response = get_status()
    json_data = response.json()
    is_valid = validate_json_schema(json_data, status_schema)
    return is_valid


def validate_all_products_json():
    all_products_schema = json.loads(open('../json_schema/all_products_schema.txt').read())
    response = get_all_products()
    json_data = response.json()
    is_valid = validate_json_schema(json_data, all_products_schema)
    return is_valid


def validate_coffee_products_json():
    coffee_products_schema = json.loads(open('../json_schema/coffee_products_schema.txt').read())
    response = get_products_list_by_category('coffee')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, coffee_products_schema)
    return is_valid


def validate_fresh_produce_products_json():
    fresh_produce_products_schema = json.loads(open('../json_schema/fresh_produce_products_schema.txt').read())
    response = get_products_list_by_category('fresh-produce')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, fresh_produce_products_schema)
    return is_valid


def validate_meat_seafood_products_json():
    meat_seafood_products_schema = json.loads(open('../json_schema/meat_seafood_products_schema.txt').read())
    response = get_products_list_by_category('meat-seafood')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, meat_seafood_products_schema)
    return is_valid


def validate_candy_products_json():
    candy_products_schema = json.loads(open('../json_schema/candy_products_schema.txt').read())
    response = get_products_list_by_category('candy')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, candy_products_schema)
    return is_valid


def validate_dairy_products_json():
    dairy_products_schema = json.loads(open('../json_schema/dairy_products_schema.txt').read())
    response = get_products_list_by_category('dairy')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, dairy_products_schema)
    return is_valid


def validate_bread_bakery_products_json():
    bread_bakery_products_schema = json.loads(open('../json_schema/bread_bakery_products_schema.txt').read())
    response = get_products_list_by_category('bread-bakery')
    json_data = response.json()
    is_valid = validate_json_schema(json_data, bread_bakery_products_schema)
    return is_valid


def validate_cart_json():
    cart_schema = json.loads(open('../json_schema/cart_schema.txt').read())
    response = create_a_cart()
    json_data = response.json()
    is_valid = validate_json_schema(json_data, cart_schema)
    return is_valid


def validate_add_item_to_cart_json(response):
    add_item_to_cart_schema = json.loads(open('../json_schema/add_item_to_cart_schema.txt').read())
    json_data = response.json()
    is_valid = validate_json_schema(json_data, add_item_to_cart_schema)
    return is_valid


def validate_get_cart_items_json(response):
    get_cart_items_schema = json.loads(open('../json_schema/get_cart_items_schema.txt').read())
    json_data = response.json()
    is_valid = validate_json_schema(json_data, get_cart_items_schema)
    return is_valid


def validate_create_new_order_json(response):
    create_new_order_schema = json.loads(open('../json_schema/create_new_order_schema.txt').read())
    json_data = response.json()
    is_valid = validate_json_schema(json_data, create_new_order_schema)
    return is_valid


def validate_single_order_json(r):
    single_order_schema = json.loads(open('../json_schema/single_order_schema.txt').read())
    json_data = r.json()
    is_valid = validate_json_schema(json_data, single_order_schema)
    return is_valid
