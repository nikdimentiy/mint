import pandas as pd

# Prompt user for data
player1_odds = float(input("Enter the odds for Player 1: "))
player2_odds = float(input("Enter the odds for Player 2: "))

# Calculate implied probabilities
player1_prob = (1 / player1_odds) * 100
player2_prob = (1 / player2_odds) * 100

# Check for arbitrage opportunity
total_prob = player1_prob + player2_prob
if total_prob < 100:
    opportunity = "Yes"
    # Calculate betting amounts
    bet1 = (player2_prob / total_prob) * 100
    bet2 = (player1_prob / total_prob) * 100
    bet_info = "Bet {:.2f} units on Player 1 and {:.2f} units on Player 2.".format(bet2, bet1)
else:
    opportunity = "No"
    bet_info = ""

# Create dataframe and save to csv file
data = {
    'Player 1 Odds': [player1_odds],
    'Player 2 Odds': [player2_odds],
    'Arbitrage Opportunity': [opportunity],
    'Betting Information': [bet_info],
}
df = pd.DataFrame(data)
df.to_csv('betting_info.csv', index=False)