// The code represents and calculates many recursion algorithms:
// factorial, greatest common divisor, fast degree of the number,
// and Fibonacci sequence (needed member - the number)
#include <stdio.h>

int factorial(int n) {
    if (0 == n)
        return 1;
    return factorial(n - 1) * n;
}

int gcd(int a, int b) {
    if (0 == b) return a;
    return gcd(b, a % b);
}

double fast_degree(double a, int n) {
    if (0 == n) return 1;
    if (n % 2 == 1)
        return a * fast_degree(a, n - 1);
    else
        return fast_degree(a * a, n / 2);
}

int fib(int n) {
    if (n <= 1) return n;
    else return fib(n - 1) + fib(n - 2);
}

int main(void) {
    int n, m;
    printf("Enter 2 (two) integers number:\n");
    printf("First integer - for calculate: factorial of entered number, fast degree and number of sequence Fibonacci: \n");
    scanf("%d", &n);
    printf("Second integer - for calculate: greatest common divisor: \n");
    scanf("%d", &m);
    printf("\n");
    printf("The Factorial(%d) = %d\n", n, factorial(n));
    printf("Greatest common divisor(%d, %d) = %d\n", n, m, gcd(n, m));
    printf("Fast degree(%d, %d) = %lf\n", n, m, fast_degree(n, m));
    printf("Number(member) of sequence Fibonacci(%d) = %d\n", n, fib(n));

    return 0;
}