def describe_pet(pet_name, animal_type='dog'):
    """Show information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('willie', animal_type="cat")
