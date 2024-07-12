/**
 * @file mathematical_functions.c
 * @brief Implements several common mathematical functions.
 * 
 * This program demonstrates the use of recursive and iterative algorithms to
 * compute:
 * - Factorial of a number
 * - Greatest Common Divisor (GCD) of two numbers
 * - Fast exponentiation (power) of a base number
 * - Fibonacci number at a given position
 * 
 * The `main()` function reads two integers from the user and then computes and
 * displays the results of these mathematical functions.
 * 
 * - `factorial(int n)`: Computes the factorial of `n`.
 * - `gcd(int a, int b)`: Computes the greatest common divisor of `a` and `b`.
 * - `fast_power(double a, int n)`: Computes `a` raised to the power `n` using a fast exponentiation algorithm.
 * - `fib(int n)`: Computes the `n`-th Fibonacci number.
 * 
 * Example usage:
 * Input: 
 *   5 3
 * Output:
 *   factorial(5) = 120
 *   gcd(5, 3) = 1
 *   fast_power(5, 3) = 125.000000
 *   fib(5) = 5
 */

#include <stdio.h>

/**
 * @brief Computes the factorial of a non-negative integer n.
 * 
 * The factorial of a number `n` is defined as the product of all positive integers less than or equal to `n`.
 * It is denoted as `n!`.
 * 
 * @param n Non-negative integer for which the factorial is to be computed.
 * @return The factorial of `n`.
 */
int factorial(int n)
{
    if (0 == n)
        return 1;  // Base case: factorial of 0 is 1
    return factorial(n-1) * n;  // Recursive case
}

/**
 * @brief Computes the Greatest Common Divisor (GCD) of two integers a and b.
 * 
 * The GCD of two integers is the largest positive integer that divides both of them without a remainder.
 * This implementation uses the Euclidean algorithm.
 * 
 * @param a First integer.
 * @param b Second integer.
 * @return The GCD of `a` and `b`.
 */
int gcd(int a, int b)
{
    if (0 == b)
        return a;  // Base case: when the second number is 0, return the first number
    return gcd(b, a % b);  // Recursive case: Euclidean algorithm
}

/**
 * @brief Computes `a` raised to the power `n` using a fast exponentiation algorithm.
 * 
 * This function uses the method of exponentiation by squaring, which is efficient for large powers.
 * 
 * @param a Base value.
 * @param n Exponent.
 * @return `a` raised to the power of `n`.
 */
double fast_power(double a, int n)
{
    if (0 == n)
        return 1;  // Base case: any number to the power of 0 is 1
    if (n % 2 == 1)
        return a * fast_power(a, n - 1);  // Recursive case for odd exponents
    else
        return fast_power(a * a, n / 2);  // Recursive case for even exponents
}

/**
 * @brief Computes the n-th Fibonacci number.
 * 
 * The Fibonacci sequence is defined as follows: `fib(0) = 0`, `fib(1) = 1`, and for `n > 1`, `fib(n) = fib(n-1) + fib(n-2)`.
 * 
 * @param n The position in the Fibonacci sequence.
 * @return The Fibonacci number at position `n`.
 */
int fib(int n)
{
    if (n <= 1)
        return n;  // Base case: Fibonacci of 0 or 1 is the number itself
    else
        return fib(n-1) + fib(n-2);  // Recursive case
}

/**
 * @brief Main function to read input and display results of mathematical functions.
 * 
 * Reads two integers from the user, computes their factorial, GCD, fast power, and Fibonacci number,
 * and then prints the results.
 * 
 * @param argc Number of command-line arguments.
 * @param argv Array of command-line argument strings.
 * @return int Exit status of the program.
 */
int main(int argc, char* argv[])
{
    int n, m;

    // Read two integers from standard input
    scanf("%d%d", &n, &m);

    // Calculate and display the results of the functions
    printf("factorial(%d) = %d\n", n, factorial(n));
    printf("gcd(%d, %d) = %d\n", n, m, gcd(n, m));
    printf("fast_power(%d, %d) = %lf\n", n, m, fast_power(n, m));
    printf("fib(%d) = %d\n", n, fib(n));

    return 0;  // Exit the program
}

