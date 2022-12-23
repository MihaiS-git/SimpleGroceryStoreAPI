import json
import requests
from api_utils.api_utils import *


"""API REQUEST FUNCTIONS"""


def get_status():
    r = requests.get(f'{API_URL}/status')
    return r


def get_api_head():
    r = requests.head(f'{API_URL}')
    return r


def get_all_products():
    r = requests.get(f'{API_URL}/products')
    return r


def get_products_list_by_category(category):
    if category == "coffee":
        r = requests.get(API_URL + parameters[category])
        return r
    elif category == "fresh-produce":
        r = requests.get(API_URL + parameters[category])
        return r
    elif category == "meat-seafood":
        r = requests.get(API_URL + parameters[category])
        return r
    elif category == "candy":
        r = requests.get(API_URL + parameters[category])
        return r
    elif category == "dairy":
        r = requests.get(API_URL + parameters[category])
        return r
    elif category == "bread-bakery":
        r = requests.get(API_URL + parameters[category])
        return r


def get_a_product_by_id(product_id):
    r = requests.get(f'{API_URL}/products/{product_id}')
    return r


def create_a_cart():
    r = requests.post(f'{API_URL}/carts')
    return r


def add_product_to_cart(cart_id, product_id, quantity=1):
    payload = {
        "productId": product_id,
        "quantity": quantity
    }
    r = requests.post(f'{API_URL}/carts/{cart_id}/items', json=payload)
    return r


def get_cart_items(cart_id):
    r = requests.get(f'{API_URL}/carts/{cart_id}/items')
    return r


def modify_cart_items_quantity(cart_id, item_id, quantity):
    payload = {
        "quantity": quantity
    }
    r = requests.patch(f'{API_URL}/carts/{cart_id}/items/{item_id}', json=payload)
    return r


def replace_item_in_cart(cart_id, item_id, product_id, quantity=1):
    payload = {
        "productId": product_id,
        "quantity": quantity
    }
    r = requests.put(f'{API_URL}/carts/{cart_id}/items/{item_id}', json=payload)
    return r


def delete_item_in_cart(cart_id, item_id):
    r = requests.delete(f'{API_URL}/carts/{cart_id}/items/{item_id}')
    return r


def register_api_client_new_credentials():
    client_name = generate_unique_client_name()
    client_email = generate_unique_client_email()
    payload = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    r = requests.post(f'{API_URL}/api-clients', json=payload)
    access_token = r.json()['accessToken']
    with open('../api_utils/client_token.txt', 'w') as file:
        file.write(access_token)
    with open('../api_utils/client_credentials.txt', 'w') as file:
        json.dump(payload["clientName"], file)
    return r


def register_api_client_registered_name():
    client_name = "John_Doe8581996"
    client_email = generate_unique_client_email()
    payload = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    r = requests.post(f'{API_URL}/api-clients', json=payload)
    access_token = r.json()['accessToken']
    with open('../api_utils/client_token.txt', 'w') as file:
        file.write(access_token)
    with open('../api_utils/client_credentials.txt', 'w') as file:
        json.dump(payload["clientName"], file)
    with open('../api_utils/client_email.txt', 'w') as file:
        json.dump(payload["clientEmail"], file)
    return r


def register_api_client_registered_email():
    client_name = "John_Doe8581996"
    client_email = "John_Doe2156471@example.com"
    payload = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    r = requests.post(f'{API_URL}/api-clients', json=payload)
    try:
        access_token = r.json()['accessToken']
        with open('../api_utils/client_token.txt', 'w') as file:
            file.write(access_token)
        with open('../api_utils/client_credentials.txt', 'w') as file:
            json.dump(payload["clientName"], file)
    except KeyError:
        print("Error: API client already registered. Try a different email.")
    return r


def create_new_order_good_credentials(cart_id):
    payload = {
        "cartId": cart_id,
        "customerName": get_client_name()
    }
    token = get_client_token()
    headers = {
        "Authorization": token,
    }
    r = requests.post(f'{API_URL}/orders', json=payload, headers=headers)
    return r


def create_new_order_fake_credentials(cart_id):
    payload = {
        "cartId": cart_id,
        "customerName": get_client_name()
    }
    token = get_client_token()
    headers = {
        "Authorization": f'{token}*111',
    }
    r = requests.post(f'{API_URL}/orders', json=payload, headers=headers)
    return r


def get_all_orders_good_credentials():
    token = get_client_token()
    headers = {
        "Authorization": token,
    }
    r = requests.get(f'{API_URL}/orders', headers=headers)
    return r


def get_all_orders_fake_credentials():
    token = get_client_token()
    headers = {
        "Authorization": f'{token}*111',
    }
    r = requests.get(f'{API_URL}/orders', headers=headers)
    return r


def update_order_good_credentials(order_id, comment):
    token = get_client_token()
    headers = {
        "Authorization": token,
    }
    payload = {
        "customerName": "Mihai",
        "comment": comment
    }
    r = requests.patch(f'{API_URL}/orders/{order_id}', json=payload, headers=headers)
    return r


def update_order_fake_credentials(order_id, comment):
    token = get_client_token()
    headers = {
        "Authorization": f'{token}*111',
    }
    payload = {
        "customerName": "Mihai",
        "comment": comment
    }
    r = requests.patch(f'{API_URL}/orders/{order_id}', json=payload, headers=headers)
    return r


def get_a_single_order_good_credentials(order_id):
    token = get_client_token()
    headers = {
        "Authorization": token,
    }
    r = requests.get(f'{API_URL}/orders/{order_id}', headers=headers)
    return r


def get_a_single_order_fake_credentials(order_id):
    token = get_client_token()
    headers = {
        "Authorization": f'{token}*111',
    }
    r = requests.get(f'{API_URL}/orders/{order_id}', headers=headers)
    return r


def delete_an_order_good_credentials(order_id):
    token = get_client_token()
    headers = {
        "Authorization": token,
    }
    r = requests.delete(f'{API_URL}/orders/{order_id}', headers=headers)
    return r


def delete_an_order_fake_credentials(order_id):
    token = get_client_token()
    headers = {
        "Authorization": f'{token}*111',
    }
    r = requests.delete(f'{API_URL}/orders/{order_id}', headers=headers)
    return r
