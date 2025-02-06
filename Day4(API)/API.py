import requests 
import json
class Rest_API:
    def fetch_and_store_data(self):
        response = requests.get('https://dummyjson.com/products')
        data = response.json()

        # Store the data into a JSON file
        with open(r'D:\ApexaIQ\Day4\products_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return data

    