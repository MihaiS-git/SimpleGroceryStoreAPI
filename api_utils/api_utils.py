import random
from api_requests.api_requests import *

"""Base URL"""


API_URL = 'https://simple-grocery-store-api.glitch.me'


"""Functions URL parameters"""


parameters = {
    'coffee': f'/products?category=coffee',
    'fresh-produce': f'/products?category=fresh-produce',
    'meat-seafood': f'/products?category=meat-seafood',
    'candy': f'/products?category=candy',
    'dairy': f'/products?category=dairy',
    'bread-bakery': f'/products?category=bread-bakery'
}


"""GENERAL USE FUNCTIONS"""


def generate_unique_client_name():
    unique_number = random.randint(1000000, 9999999)
    unique_client_name = f"John_Doe{unique_number}"
    return unique_client_name


def generate_unique_client_email():
    unique_number = random.randint(1000000, 9999999)
    unique_client_email = f"John_Doe{unique_number}@example.com"
    return unique_client_email


def get_client_token():
    with open('../api_utils/client_token.txt', 'r') as file:
        client_token = file.read()
    return client_token


def get_client_name():
    with open('../api_utils/client_credentials.txt', 'r') as file:
        client_name = file.read()
    return client_name
