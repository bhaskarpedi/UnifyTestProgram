from sortedlibrary import *
import json

def test_get_available_pets_success():
    request = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    response = get_availabe_pets(request)
    assert(isinstance(response, list))

def test_get_available_pets_failure():
    request = "Testing failure case"
    response = get_availabe_pets(request)
    assert("Error occurred during request!!" in response)

def test_sort_by_name():
    pets = [{"name":""}, {"name":"!@#%"}, {"name": "Zorro"}, {"name": "Brooney"}, {"name":"Anpome"}, {"name":"Aabeeble","tags": [ {"id":0, "name":"Zorro"}]}]
    sorted_pets = [{'name': 'Zorro'}, {'name': 'Brooney'}, {'name': 'Anpome'}, {"name":"Aabeeble","tags": [ {"id":0, "name":"Zorro"}]}, {'name': '!@#%'}, {'name': ''}]
    assert(sort_by_name(pets) == sorted_pets)
