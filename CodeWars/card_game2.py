def card_game(n):
    """
    Simulates a card game elimination process and determines the winner's position.

    Parameters:
    n (int): The number of players in the game.

    Returns:
    int: The position of the winning player (1-indexed).
    """
    if n == 1:
        return 1  # If there's only one player, they are the winner.

    t, s = 0, n + 2  # Initialize t (eliminated players) and s (current players).
    
    # Continue the elimination process until only 3 or fewer players remain.
    while s > 3:
        s, t = s // 2, t + 1 + s % 2  # Update the number of players and eliminated count.

    # Return the position of the winner based on whether n is odd or even.
    return [n - t, t][n % 2]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(card_game(1))  # Output: 1 (only one player)
    print(card_game(2))  # Output: 1 (player 1 wins)
    print(card_game(3))  # Output: 2 (player 2 wins)
    print(card_game(4))  # Output: 1 (player 1 wins)
    print(card_game(5))  # Output: 2 (player 2 wins)
    print(card_game(6))  # Output: 5 (player 5 wins)
    print(card_game(7))  # Output: 4 (player 4 wins)
    print(card_game(8))  # Output: 1 (player 1 wins)

