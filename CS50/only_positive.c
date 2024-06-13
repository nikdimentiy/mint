/**
 * @file get_positive_integer.c
 * @brief A program to prompt the user for a positive integer.
 *
 * This program contains a function to repeatedly prompt the user
 * to enter a positive integer until a valid input is provided. The
 * valid input is then displayed back to the user.
 */

#include <stdio.h>

/**
 * @brief Prompts the user for a positive integer.
 * 
 * This function repeatedly prompts the user to enter a positive
 * integer until the user provides a valid input. It ensures the input
 * is greater than zero.
 * 
 * @return int Returns the positive integer provided by the user.
 */
int GetPositiveInt(void)
{
    int n;
    // Loop until a valid positive integer is entered
    do 
    {
        printf("Please give me a positive integer number: ");
        scanf("%i", &n);
    }
    while (n < 1); // Continue prompting until a positive integer is entered
    return n;
}   

/**
 * @brief Main function to execute the positive integer input program.
 * 
 * This function calls GetPositiveInt to obtain a positive integer from
 * the user and then displays a thank you message with the provided number.
 * 
 * @return int Returns 0 upon successful execution.
 */
int main(void)
{
    int n = GetPositiveInt(); // Get a positive integer from the user
    printf("Thanks for the %i!\n", n); // Display a thank you message with the input
    return 0; // Indicate successful execution
}
