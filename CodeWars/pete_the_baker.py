def cakes(recipe, available):
    """
    Calculate the maximum number of cakes that can be baked given a recipe and available ingredients.

    Parameters:
    recipe (dict): A dictionary where the keys are ingredient names (str) and the values are the amounts needed (int) for one cake.
    available (dict): A dictionary where the keys are ingredient names (str) and the values are the amounts available (int).

    Returns:
    int: The maximum number of cakes that can be baked. If any ingredient in the recipe is not available, returns 0.
    """
    # Create a list of how many cakes can be made with each ingredient
    # If the ingredient is not available, it contributes 0 to the list.
    cakes_possible = [
        available[i] // recipe[i] if i in available else 0 
        for i in recipe
    ]
    
    # Return the minimum value from the list, which represents the limiting ingredient
    return min(cakes_possible)

# Driver code to test the function
if __name__ == "__main__":
    # Example recipe and available ingredients
    recipe = {
        'flour': 500,
        'sugar': 200,
        'eggs': 1
    }
    
    available = {
        'flour': 1200,
        'sugar': 1200,
        'eggs': 5,
        'milk': 200  # This ingredient is not in the recipe and will be ignored
    }
    
    # Calculate the maximum number of cakes that can be baked
    max_cakes = cakes(recipe, available)
    print(f"Maximum number of cakes that can be baked: {max_cakes}")
