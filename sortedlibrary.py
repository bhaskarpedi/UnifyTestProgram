# Test function to build test scaffolding
import requests
import json

def get_availabe_pets(request_url):
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            available_pets = json.loads(response.content)
            return available_pets
        else:
            raise Exception(response.status_code)
    except Exception as e:
        return(f"Error occurred during request!! \n {e}")