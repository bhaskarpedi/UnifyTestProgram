from sortedlibrary import *

# Script starts running here
if __name__ == '__main__':
    # Requirement 1: Return a list of available Pets from the Pet Store
    # Request for all pets with available status
    available_pets = get_availabe_pets("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    print(json.dumps(available_pets, indent=2, sort_keys=False))

    # Print a list of available Pets to the console sorted in Categories and displayed in reverse order by Name
    # Create a dictionary with categories and the pets that map to that category
    # Assumption: As the ID of the category is not unique, assume that the combination of id and name is the unique key (convert to string and use as key for dictionary)
    categorized_pets = dict()
    categorized_pets["uncategorized"] = list()
    
    for pet in available_pets:
        if 'category' not in pet:
            categorized_pets["uncategorized"].append(pet)
        else:
            if json.dumps(pet['category']) not in categorized_pets.keys():
                categorized_pets[json.dumps(pet['category'])] = list()
            categorized_pets[json.dumps(pet['category'])].append(pet)
    
    print("\n\n\nFollowing are the available pets sorted in categories and displayed in reverse order")

    for key in categorized_pets:
        print(f"\n\nCategory: {key}")
        print(json.dumps(sort_by_name(categorized_pets[key]), indent=2, sort_keys=False))
    
