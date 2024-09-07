def solution(n, m):
    """
    Calculate the total number of pieces of candy that can be eaten by all children.

    Each child must eat the same amount of candy, and individual pieces of candy cannot be split.
    
    Parameters:
    n (int): The number of children.
    m (int): The total number of pieces of candy available.

    Returns:
    int: The total number of pieces of candy that will be eaten by all children together.
    """
    # Calculate how many pieces of candy each child can eat
    candies_per_child = m // n
    
    # Calculate the total candies eaten by all children
    total_candies = candies_per_child * n
    
    return total_candies

# Driver code to test the solution function
if __name__ == "__main__":
    # Example 1: 3 children and 10 pieces of candy
    n1, m1 = 3, 10
    print(f"Total candies eaten by {n1} children with {m1} pieces of candy: {solution(n1, m1)}")

    # Example 2: 5 children and 22 pieces of candy
    n2, m2 = 5, 22
    print(f"Total candies eaten by {n2} children with {m2} pieces of candy: {solution(n2, m2)}")

    # Example 3: 4 children and 15 pieces of candy
    n3, m3 = 4, 15
    print(f"Total candies eaten by {n3} children with {m3} pieces of candy: {solution(n3, m3)}")

    # Example 4: 0 children and 10 pieces of candy (edge case)
    n4, m4 = 0, 10
    print(f"Total candies eaten by {n4} children with {m4} pieces of candy: {solution(n4, m4) if n4 > 0 else 0}")
