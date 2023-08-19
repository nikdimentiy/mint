def is_prime(n):
  """
  Check if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """
  # If the number is less than or equal to 1, it's not prime.
  if n <= 1:
    return False

  # Check divisibility from 2 up to the square root of n.
  for i in range(2, int(n ** 0.5) + 1):
    # If n is divisible by i, it's not prime.
    if n % i == 0:
      return False

  # If no divisors are found, the number is prime.
  return True


def main():
  """Find all prime numbers from 0 to 10000 and print them out."""
  primes = []

  # Iterate through numbers from 2 to 10000.
  for i in range(2, 10001):
    # Check if the current number is prime using the is_prime function.
    if is_prime(i):
      # If prime, add it to the list of primes.
      primes.append(i)

  # Print the list of prime numbers.
  print("The prime numbers from 0 to 10000 are:")
  for prime in primes:
    print(prime)


if __name__ == "__main__":
  # Call the main function if this script is run directly.
  main()

