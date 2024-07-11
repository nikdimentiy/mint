#include <stdio.h>

/**
 * @file sum_of_digits.c
 * @brief This program computes the sum of the digits of an entered integer.
 *
 * The program defines a function to calculate the sum of the digits of an
 * integer. It then prompts the user to enter an integer, computes the sum
 * of its digits using the defined function, and prints the result.
 */

/**
 * @brief Computes the sum of the digits of an integer.
 *
 * This function takes an integer as input and iteratively extracts each digit,
 * adding it to a running total until all digits have been processed.
 *
 * @param n The integer whose digits are to be summed.
 * @return The sum of the digits of the integer.
 */
int getSum(int n) 
{ 
    int sum = 0; 

    // Loop to extract and sum each digit of the number
    while (n != 0) 
    { 
        sum = sum + n % 10; // Add the last digit to sum
        n = n / 10; // Remove the last digit
    } 

    return sum; 
} 

/**
 * @brief Main function to read an integer from the user and print the sum of its digits.
 *
 * Prompts the user to enter an integer, calculates the sum of its digits using
 * the getSum function, and prints the result.
 *
 * @return int Returns 0 upon successful execution.
 */
int main() 
{
    int n;

    // Prompt the user to enter an integer
    printf("Enter an integer number: \n");
    scanf("%d", &n);

    // Compute and print the sum of digits of the entered number
    printf("The sum of digits of the entered number is: %d\n", getSum(n)); 

    return 0; 
}
