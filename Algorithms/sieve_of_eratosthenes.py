def sieve_of_eratosthenes(N):
    """
    Generate a list indicating whether each number up to N is prime or composite.
    
    Parameters:
    N (int): The upper limit for the range of numbers to check.
    
    Returns:
    list: A list of boolean values indicating whether each number is prime.
    """
    A = [True] * N
    A[0] = A[1] = False  # 0 and 1 are not prime
    
    for k in range(2, N):
        if A[k]:
            # Mark the multiples of k as composite
            for m in range(2 * k, N, k):
                A[m] = False
    
    return A

def print_prime_or_composite(A):
    """
    Print whether each number up to the length of A is prime or composite.
    
    Parameters:
    A (list): A list of boolean values indicating whether each number is prime.
    """
    for k in range(len(A)):
        print(k, "-", "prime" if A[k] else "composite")

# Define the upper limit N
N = 100

# Generate the list of prime indicators using the Sieve of Eratosthenes algorithm
prime_indicators = sieve_of_eratosthenes(N)

# Print whether each number is prime or composite
print_prime_or_composite(prime_indicators)

