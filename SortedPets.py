from sortedlibrary import *

# Script starts running here
if __name__ == '__main__':
    # Requirement 1: Return a list of available Pets from the Pet Store
    # Request for all pets with available status
    available_pets = get_availabe_pets("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    print(json.dumps(available_pets, indent=2, sort_keys=False))

    # Print a list of available Pets to the console sorted in Categories and displayed in reverse order by Name
    

