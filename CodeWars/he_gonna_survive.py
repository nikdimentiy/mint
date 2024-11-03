def hero(bullets, dragons):
    """
    Determine if the hero has enough bullets to defeat the dragons.

    Parameters:
    bullets (int): The number of bullets the hero has.
    dragons (int): The number of dragons the hero needs to defeat.

    Returns:
    bool: True if the hero has enough bullets to defeat all dragons, 
          False otherwise. The hero needs 2 bullets for each dragon.
    """
    # Check if the number of bullets is at least twice the number of dragons
    return bullets >= 2 * dragons

# Driver code to test the hero function
if __name__ == "__main__":
    # Test cases
    print(hero(10, 5))  # Expected output: True (10 >= 2*5)
    print(hero(7, 3))   # Expected output: False (7 < 2*3)
    print(hero(0, 0))   # Expected output: True (0 >= 2*0)
    print(hero(4, 2))   # Expected output: True (4 >= 2*2)
    print(hero(5, 3))   # Expected output: False (5 < 2*3)
