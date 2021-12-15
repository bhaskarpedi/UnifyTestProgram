# Test function to build test scaffolding
import requests
import json

# Request for available pets and return them as a list or return any errors that we see
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

def sort_by_name(pet_list, reverse=True):
    return sorted(pet_list,reverse=reverse, key=lambda x: x['name'])

