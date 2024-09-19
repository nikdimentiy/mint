def card_game(n):
    """
    Calculate the number of cards in a game based on the given integer n.

    The function uses a recursive approach to determine the number of cards 
    based on the following rules:
    - For n <= 4, it returns predefined values.
    - If n is odd, it returns n minus the result of card_game(n - 1).
    - If n is even and not divisible by 4, it returns n // 2 plus the result of card_game(n // 2 - 1).
    - If n is even and divisible by 4, it returns 1 plus the result of card_game(n - 2).

    Parameters:
    n (int): The number of cards to evaluate.

    Returns:
    int: The calculated number of cards.
    """
    # Base cases for small values of n
    if n <= 4:
        return [0, 1, 1, 2, 3][n]
    
    # If n is odd, use the recursive formula for odd numbers
    if n & 1:
        return n - card_game(n - 1)
    
    # If n is even and not divisible by 4, use the recursive formula for even numbers
    if n & 2:
        return n // 2 + card_game(n // 2 - 1)
    
    # If n is even and divisible by 4, use the recursive formula for this case
    return 1 + card_game(n - 2)

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
    for n in test_cases:
        result = card_game(n)
        print(f"card_game({n}) = {result}")
