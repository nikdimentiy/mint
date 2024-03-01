import csv

def process_stock_prices(csv_file_path):
    """
    Reads stock prices from a CSV file and performs calculations.

    Args:
        csv_file_path (str): The path to the CSV file containing stock price data.

    Returns:
        list: A list of stock prices.
        float: The total sum of stock prices.
        float: The maximum stock price.
    """
    stock_prices = []

    # Open the CSV file in read mode
    with open(csv_file_path) as data_file:
        # Create a CSV reader object
        reader = csv.reader(data_file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the row is not a header
            if row[1] != "Current Price":
                # Convert the stock price to float and add it to the list
                stock_prices.append(float(row[1]))

    # Print the list of stock prices
    print("Stock Prices:", stock_prices)

    # Calculate the total sum of stock prices
    total_sum = sum(stock_prices)
    # Print the total sum of stock prices
    print("Total Sum:", total_sum)

    # Find the maximum stock price
    max_price = max(stock_prices)
    # Print the maximum stock price
    print("Maximum Price:", max_price)

    return stock_prices, total_sum, max_price

# Path to the CSV file containing stock price data
csv_file_path = "quotes.csv"

# Process stock prices from the CSV file
stock_prices, total_sum, max_price = process_stock_prices(csv_file_path)
