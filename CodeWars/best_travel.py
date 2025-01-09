def choose_best_sum(t, k, ls):
    """
    Find the maximum sum of k distances that does not exceed a given limit from a list of distances.
    
    This function finds the optimal combination of k distances from the given list that sum up to
    a value closest to but not exceeding the target value t. It uses a recursive approach to
    generate all possible combinations.
    
    Parameters:
        t (int): The target sum (maximum limit) of distances
        k (int): The number of towns/distances to include in the sum
        ls (list): List of integers representing distances between towns
        
    Returns:
        int or None: The maximum possible sum of k distances that doesn't exceed t,
                    or None if no such combination exists
    
    Examples:
        >>> ts = [50, 55, 56, 57, 58]
        >>> choose_best_sum(163, 3, ts)  # should return 163
        >>> choose_best_sum(163, 3, [50])  # should return None (not enough towns)
        >>> choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87])  # should return 228
    """
    
    def get_combinations(sum_so_far, towns_left):
        """
        Helper function to recursively generate all possible combinations of k towns.
        
        Args:
            sum_so_far (list): Current combination being built
            towns_left (list): Remaining towns to choose from
            
        Returns:
            list: List of all possible combinations of k towns
        """
        # Base case: not enough towns left to form a valid combination
        if len(towns_left) < k - len(sum_so_far):
            return []
        
        # Base case: we have selected exactly k towns
        elif len(sum_so_far) == k:
            return [sum_so_far]
        
        # Recursive case: try adding each remaining town to our combination
        else:
            combos = []
            for i, town in enumerate(towns_left):
                # Add current town and recursively generate combinations with remaining towns
                new_combos = get_combinations(sum_so_far + [town], towns_left[i+1:])
                combos.extend(new_combos)
            return combos
    
    # Generate all possible combinations of k towns
    town_combinations = get_combinations([], ls)
    
    # Calculate the sum of distances for each valid combination
    sums = [sum(combination) for combination in town_combinations]
    
    # Find the maximum sum that doesn't exceed t
    max_sum = max(filter(lambda x: x <= t, sums), default=None)
    
    return max_sum

# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Basic case with exact sum possible
    ts = [50, 55, 56, 57, 58]
    result1 = choose_best_sum(163, 3, ts)
    print(f"Test 1: Target=163, k=3, Result={result1}")  # Expected: 163
    
    # Test case 2: Case with not enough towns
    result2 = choose_best_sum(163, 3, [50])
    print(f"Test 2: Target=163, k=3, Result={result2}")  # Expected: None
    
    # Test case 3: Case with multiple possible combinations
    ts2 = [91, 74, 73, 85, 73, 81, 87]
    result3 = choose_best_sum(230, 3, ts2)
    print(f"Test 3: Target=230, k=3, Result={result3}")  # Expected: 228
    
    # Test case 4: Edge case with empty list
    result4 = choose_best_sum(163, 3, [])
    print(f"Test 4: Target=163, k=3, Result={result4}")  # Expected: None
    
    # Test case 5: Case where sum exactly equals target
    ts3 = [50, 50, 50, 50]
    result5 = choose_best_sum(150, 3, ts3)
    print(f"Test 5: Target=150, k=3, Result={result5}")  # Expected: 150
