# Prompt user for data
player1_odds = float(input("Enter the odds for Player 1: "))
player2_odds = float(input("Enter the odds for Player 2: "))

# Calculate implied probabilities
player1_prob = (1 / player1_odds) * 100
player2_prob = (1 / player2_odds) * 100

# Check for arbitrage opportunity
total_prob = player1_prob + player2_prob
if total_prob < 100:
    print("There is an opportunity for arbitrage!")
    # Calculate betting amounts
    bet1 = (player2_prob / total_prob) * 100
    bet2 = (player1_prob / total_prob) * 100
    print("Bet {:.2f} units on Player 1 and {:.2f} units on Player 2.".format(bet2, bet1))
else:
    print("There is no opportunity for arbitrage.")