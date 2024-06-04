#include <stdio.h>

/**
 * Function to get the prime factors of a given number.
 *
 * This function finds the prime factors of the given integer x and stores them in the provided array A.
 * It returns the number of prime factors found.
 *
 * @param x The number to be factorized.
 * @param A An array to store the prime factors. The caller must ensure this is large enough.
 * @return The number of prime factors stored in A.
 */
int get_number_factors(int x, int A[]) {
    int top = 0;         // Index to keep track of the position in the array A
    int divisor = 2;     // The current divisor to check for factorization

    // Loop until x is reduced to 1
    while (x != 1) {
        // Check if divisor is a factor of x
        while (x % divisor == 0) {
            A[top] = divisor;  // Store the divisor in the array A
            top += 1;          // Move to the next position in the array
            x /= divisor;      // Divide x by the divisor
        }
        divisor += 1;          // Move to the next potential divisor
    }
    return top;  // Return the number of factors found
}

int main(int argc, char* argv[]) {
    int x;  // Variable to store the input number
    printf("Enter number to factorize: ");
    scanf("%d", &x);

    int A[100];  // Array to store the prime factors (assuming a max of 100 factors)
    int N;       // Variable to store the number of factors found

    // Get the prime factors of x
    N = get_number_factors(x, A);

    // Print the prime factors
    for(int i = 0; i < N; ++i) {
        printf("%d ", A[i]);
    }
    printf("\n");

    return 0;
}
