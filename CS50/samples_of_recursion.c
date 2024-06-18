#include <stdio.h>

/**
 * Computes the factorial of a given number n.
 * 
 * @param n The number to compute the factorial of.
 * @return The factorial of n.
 */
int factorial(int n) {
    if (n == 0)
        return 1;
    return factorial(n - 1) * n;
}

/**
 * Computes the greatest common divisor (GCD) of two integers a and b.
 * 
 * @param a The first integer.
 * @param b The second integer.
 * @return The GCD of a and b.
 */
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

/**
 * Computes the result of raising a number a to the power of n using fast exponentiation.
 * 
 * @param a The base number.
 * @param n The exponent.
 * @return The result of a raised to the power of n.
 */
double fast_degree(double a, int n) {
    if (n == 0) return 1;
    if (n % 2 == 1)
        return a * fast_degree(a, n - 1);
    else
        return fast_degree(a * a, n / 2);
}

/**
 * Computes the nth Fibonacci number.
 * 
 * @param n The position in the Fibonacci sequence.
 * @return The nth Fibonacci number.
 */
int fib(int n) {
    if (n <= 1) return n;
    else return fib(n - 1) + fib(n - 2);
}

int main(void) {
    int n, m;

    // Prompt the user for input
    printf("Enter 2 (two) integers number:\n");
    printf("First integer - for calculating: factorial, fast degree, and Fibonacci sequence number:\n");
    scanf("%d", &n);
    printf("Second integer - for calculating: greatest common divisor:\n");
    scanf("%d", &m);

    // Print results of the calculations
    printf("\n");
    printf("The Factorial(%d) = %d\n", n, factorial(n));
    printf("Greatest common divisor(%d, %d) = %d\n", n, m, gcd(n, m));
    printf("Fast degree(%d, %d) = %lf\n", n, m, fast_degree((double)n, m));
    printf("Number (member) of Fibonacci sequence(%d) = %d\n", n, fib(n));

    return 0;
}
