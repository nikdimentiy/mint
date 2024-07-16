import random
from art import logo

def deal_card():
    """
    Returns a random card from the deck.
    
    Cards are represented as a list where:
    - 11 is an Ace,
    - 2-10 are face value,
    - 10 appears four times representing 10, Jack, Queen, and King.
    
    Returns:
        int: A random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Calculate the score of a list of cards.
    
    Args:
        cards (list of int): The list of cards in hand.
    
    Returns:
        int: The calculated score.
        0 if the player has a blackjack (two cards summing to 21).
    """
    # Check for a blackjack (a hand with only two cards: Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Replace Ace (11) with 1 if total score is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """
    Compare the scores of the user and the computer to determine the result.
    
    Args:
        user_score (int): The user's score.
        computer_score (int): The computer's score.
    
    Returns:
        str: The result message based on the comparison.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """
    Play a game of Blackjack.
    
    This function initiates a game, deals cards to the user and computer,
    and handles the game logic and user interactions.
    """
    print(logo)

    # Initialize user and computer hands
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check for immediate game end conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards until it reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final hands and scores
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
