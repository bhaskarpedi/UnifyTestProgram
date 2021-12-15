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