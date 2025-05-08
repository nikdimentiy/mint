def over_the_road(address: int, n: int) -> int:
  """
  Determines the house number on the opposite side of a straight street.

  The street has 'n' identical houses on each side, numbered sequentially.
  Odd numbers are on one side, increasing from 1.
  Even numbers are on the opposite side, increasing from 2.

  Args:
    address: Your house number.
    n: The number of houses on each side of the street.

  Returns:
    The house number directly across the street from your house.

  Examples:
    over_the_road(1, 3) == 6
    over_the_road(3, 3) == 4
    over_the_road(2, 3) == 5
    over_the_road(3, 5) == 8
  """
  # Calculate the total number of houses on both sides of the street.
  total_houses = n * 2
  # The house directly opposite will have a number such that the sum of
  # the two opposite house numbers is always equal to (total_houses + 1).
  opposite_address = total_houses - address + 1
  return opposite_address

# Driver code to test the function
if __name__ == "__main__":
  print(f"Opposite of house 1 on a street with 3 houses per side: {over_the_road(1, 3)}")   # Expected output: 6
  print(f"Opposite of house 3 on a street with 3 houses per side: {over_the_road(3, 3)}")   # Expected output: 4
  print(f"Opposite of house 2 on a street with 3 houses per side: {over_the_road(2, 3)}")   # Expected output: 5
  print(f"Opposite of house 3 on a street with 5 houses per side: {over_the_road(3, 5)}")   # Expected output: 8
  print(f"Opposite of house 10 on a street with 10 houses per side: {over_the_road(10, 10)}") # Expected output: 11
  print(f"Opposite of house 7 on a street with 10 houses per side: {over_the_road(7, 10)}")  # Expected output: 14
