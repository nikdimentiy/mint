#include <stdio.h>
#define N 21 // Define the size of the sieve array

/**
 * This program implements the Sieve of Eratosthenes algorithm to find all prime
 * numbers up to a defined limit N. It initializes an array where each index represents
 * a number, marks non-prime numbers (composite) with 1, and prime numbers with 0.
 * The program then prints the array indices and their corresponding prime/composite status.
 */

int main()
{
    int sieve[N] = {0}; // Initialize the sieve array with zeros

    // Implement the Sieve of Eratosthenes algorithm
    for(int i = 2; i*i < N; ++i)
    {
        // If the current number is marked as prime
        if (sieve[i] == 0)
        {
            // Mark all multiples of i as composite
            for(int k = i*i; k < N; k += i)
            {
                sieve[k] = 1; // Composite numbers are marked with 1
            }
        }
    }

    // Print the header line of numbers
    for (int i = 0; i < N; ++i)
    {
        printf("%4i", i);
    }
    printf("\n");

    // Print the corresponding sieve array values
    for (int i = 0; i < N; ++i)
    {
        printf("%4i", sieve[i]);
    }
    printf("\n");

    return 0; // Successful execution
}
