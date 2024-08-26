class Fighter:
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(fighter1, fighter2, first_attacker):
    """
    Determines the winner of a fight between two fighters.

    Each fighter takes turns attacking the other until one of them has health <= 0.
    The fighter who reduces the opponent's health to 0 or below first is declared the winner.

    Parameters:
    fighter1 (Fighter): The first fighter in the match.
    fighter2 (Fighter): The second fighter in the match.
    first_attacker (str): The name of the fighter who attacks first.

    Returns:
    str: The name of the winning fighter.
    """
    # Determine the current attacker and the opponent based on who attacks first
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    
    # Continue the fight until one fighter's health drops to 0 or below
    while cur.health > 0:        
        # The current fighter attacks the opponent
        opp.health -= cur.damage_per_attack
        
        # Swap the roles of current fighter and opponent
        cur, opp = opp, cur
    
    # Return the name of the winning fighter
    return opp.name

# Driver code to demonstrate the function
if __name__ == "__main__":
    # Create two fighter instances
    fighter1 = Fighter("Fighter A", health=100, damage_per_attack=20)
    fighter2 = Fighter("Fighter B", health=80, damage_per_attack=25)

    # Declare the winner with Fighter A attacking first
    winner = declare_winner(fighter1, fighter2, "Fighter A")
    print(f"The winner is: {winner}")

    # Reset health for another match
    fighter1.health = 100
    fighter2.health = 80

    # Declare the winner with Fighter B attacking first
    winner = declare_winner(fighter1, fighter2, "Fighter B")
    print(f"The winner is: {winner}")
