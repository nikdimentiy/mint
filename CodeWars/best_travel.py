# Code Wars task - https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python


def choose_best_sum(t, k, ls):
    """
    This function takes three parameters: t (maximum sum of distances), k (number of towns to visit), and ls (list of distances between towns).
    It returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists,
    or otherwise None.
    """
    
    # Define a recursive function to generate all possible combinations of k towns
    def get_combinations(sum_so_far, towns_left):
        # Base case: if there are not enough towns left to choose from, return an empty list
        if len(towns_left) < k - len(sum_so_far):
            return []
        # Base case: if the current combination has k towns, return it as a single-element list
        elif len(sum_so_far) == k:
            return [sum_so_far]
        # Recursive case: for each town in the remaining list, add it to the current combination and recurse on the rest of the list
        else:
            combos = [] # Initialize an empty list to store the combinations
            for i, town in enumerate(towns_left): # Loop through each town and its index in the remaining list
                combos += get_combinations(sum_so_far + [town], towns_left[i+1:]) # Add the town to the current combination and recurse on the sublist starting from the next town
            return combos # Return the list of combinations
    
    # Generate all possible combinations of k towns
    town_combinations = get_combinations([], ls) # Call the helper function with an empty list as the initial combination and ls as the full list
    
    # Calculate the sum of distances for each combination
    sums = [sum(combination) for combination in town_combinations] # Use a list comprehension to iterate over each combination and compute its sum
    
    # Return the maximum sum that is less than or equal to t
    max_sum = max(filter(lambda x: x<=t, sums), default=None) # Use filter to keep only those sums that are within t and use max to find their maximum. If no such sum exists, return None as default.
    
    return max_sum # Return final answer
