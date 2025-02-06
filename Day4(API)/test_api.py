import json
import pytest
from API import Rest_API

def test_fetch_and_store():
    # Fetch data from API
    fetch = Rest_API()
    data=fetch.fetch_and_store_data()

    # Load data from the saved JSON file
    with open(r'D:\ApexaIQ\Day4\products_data.json', 'r') as file:
        saved_data = json.load(file)

    # Assertion 1: Check if the fetched data matches the saved data
    assert data == saved_data, "Fetched data does not match saved JSON data"

    # Assertion 2: Check specific fields in the data
    assert 'products' in  data, " 'products' key is missing from the response"
    for product in data['products']:
        assert 'id' in product,f"id is missing in {product}"
        assert product['id'] and product['title'] is not None,"id should not be null for product"
        assert isinstance(product['id'],int),"id should be in integer value"
   
