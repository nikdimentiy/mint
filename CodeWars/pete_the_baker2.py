def cakes(recipe, available):
    """
    Calculate the maximum number of cakes that can be baked given a recipe and available ingredients.

    Parameters:
    recipe (dict): A dictionary where the keys are ingredient names (str) and the values are the amounts needed (int) for one cake.
    available (dict): A dictionary where the keys are ingredient names (str) and the values are the amounts available (int).

    Returns:
    int: The maximum number of cakes that can be baked. If any ingredient in the recipe is not available, returns 0.
    """
    # Calculate the maximum number of cakes for each ingredient
    # by dividing the available amount by the required amount in the recipe.
    # Use min to find the limiting ingredient.
    return min(available.get(k, 0) // recipe[k] for k in recipe)

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
