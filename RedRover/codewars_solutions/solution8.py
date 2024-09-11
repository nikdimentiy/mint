def check_alive(health: int) -> bool:
    """
    Check if an entity is alive based on their health.

    Args:
        health (int): The health value of the entity.

    Returns:
        bool: True if the entity is alive (health > 0), False otherwise.
    """
    # Check if health is greater than 0
    if health > 0:
        return True
    else:
        return False

# Driver code
if __name__ == "__main__":
    # Test cases
    print("Testing check_alive function:")
    print(f"check_alive(5): {check_alive(5)}")   # Expected output: True
    print(f"check_alive(0): {check_alive(0)}")   # Expected output: False
    print(f"check_alive(-3): {check_alive(-3)}")  # Expected output: False

    # Additional test case
    player_health = 10
    print(f"\nPlayer health: {player_health}")
    print(f"Is player alive? {check_alive(player_health)}")

