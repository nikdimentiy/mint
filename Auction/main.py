# Import necessary modules
from replit import clear
from art import logo

# Display the program logo
print(logo)

# Initialize an empty dictionary to store bids and a flag for bidding completion
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  """
  Find the highest bidder and the corresponding bid amount.

  Args:
    bidding_record (dict): A dictionary containing bidder names as keys and their respective bid amounts as values.

  Prints:
    The winner and their winning bid.
  """
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main bidding loop
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

# Driver code
# The program starts with an empty dictionary for bids and asks for user input.
# Users can enter their name and bid amount.
# The bidding continues until the user decides to stop.
# Once bidding is finished, the program finds and displays the highest bidder and their bid amount.
