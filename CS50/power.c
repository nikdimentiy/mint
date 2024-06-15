#include <stdio.h>

// Function prototype
/**
 * @brief Calculates the power of a base raised to an exponent.
 *
 * @param base The base value.
 * @param n The exponent value.
 * @return The result of base raised to the power of n.
 */
int power(int base, int n);

/**
 * @brief Main function to test the power function.
 *
 * This function prints the result of 2 raised to the power of numbers from 0 to 10.
 * 
 * @return 0 on successful execution.
 */
int main() {
  int i;
  for (i = 0; i <= 10; i++) {
    printf("Power: %d\t  Result: %d\n", i, power(2, i));
  }

  return 0;
}

/**
 * @brief Calculates the base raised to the n-th power.
 *
 * This function multiplies the base value 'base' by itself 'n' times to compute the power.
 * 
 * @param base The base value.
 * @param n The exponent value.
 * @return The result of base raised to the power of n.
 */
int power(int base, int n) {
  int i, p;
  p = 1; // Initialize p to 1 because any number to the power of 0 is 1
  for (i = 1; i <= n; i++) { // Loop from 1 to n
    p = p * base; // Multiply the current result by the base
  }
  return p; // Return the final result
}
