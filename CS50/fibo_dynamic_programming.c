#include <stdio.h>
#include <time.h>

static int cache[100] = {0}; // Cache for memoization in the recursive Fibonacci function

/**
 * @file fibonacci_timing.c
 * @brief This program calculates Fibonacci numbers using both recursive memoization
 *        and dynamic programming approaches, and measures the time taken for each calculation.
 *
 * The program prints the Fibonacci number and the time taken (in milliseconds) to compute it
 * for values from 1 to 49 using the dynamic programming approach.
 */

/**
 * @brief Computes the n-th Fibonacci number using recursive memoization.
 *
 * This function uses a static cache to store previously computed Fibonacci numbers
 * to avoid redundant calculations.
 *
 * @param n The position of the Fibonacci number to compute.
 * @return The n-th Fibonacci number.
 */
int fib(int n)
{
    if (n <= 1)
        return n;
    if (cache[n] == 0)
        cache[n] = fib(n - 1) + fib(n - 2);
    return cache[n];
}

/**
 * @brief Computes the n-th Fibonacci number using dynamic programming.
 *
 * This function uses an iterative approach to build up the Fibonacci numbers
 * from the base cases.
 *
 * @param n The position of the Fibonacci number to compute.
 * @return The n-th Fibonacci number.
 */
int fib_dynamic(int n)
{
    int Fib[n + 1]; // Array to store Fibonacci numbers up to n
    Fib[0] = 0;
    Fib[1] = 1;
    for (int i = 2; i <= n; ++i)
        Fib[i] = Fib[i - 1] + Fib[i - 2];
    return Fib[n];
}

int main(int argc, char *argv[])
{
    // Loop through Fibonacci numbers from 1 to 49
    for (int n = 1; n < 50; n += 1)
    {
        // Measure the time taken to compute the Fibonacci number using dynamic programming
        clock_t time1 = clock();
        int result = fib_dynamic(n);
        clock_t time2 = clock();
        int delta_ms = (time2 - time1) * 1000 / CLOCKS_PER_SEC;

        // Print the Fibonacci number and the time taken to compute it
        printf("fib(%d) = %d,\t time = %d ms\n", n, result, delta_ms);
    }

    return 0; // Indicate that the program ended successfully
}
