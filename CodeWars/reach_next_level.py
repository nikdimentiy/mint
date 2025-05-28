def solution(experience, threshold, reward):
    """
    Check if the player reaches the next level after gaining experience from a monster.

    The function determines if the total experience points (XP) after defeating a monster
    will meet or exceed the threshold required to level up.

    Parameters:
    experience (int): The current experience points of the player.
    threshold (int): The experience points required to reach the next level.
    reward (int): The experience points gained from defeating the monster.

    Returns:
    bool: True if the player reaches the next level, False otherwise.
    """
    # Calculate the total experience after defeating the monster
    total_experience = experience + reward
    
    # Check if the total experience meets or exceeds the threshold
    return total_experience >= threshold

# Driver code to test the solution function
if __name__ == "__main__":
    # Example values
    current_experience = 150  # Current XP
    level_threshold = 200      # XP needed to level up
    monster_reward = 70        # XP gained from defeating the monster

    # Check if the player levels up after defeating the monster
    if solution(current_experience, level_threshold, monster_reward):
        print("You have reached the next level!")
    else:
        print("You need more experience to reach the next level.")
