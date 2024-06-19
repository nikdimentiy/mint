/**
 * This program prompts the user to enter an integer number and then
 * evaluates the input using a switch statement to print different
 * messages based on the value entered.
 */

#include <stdio.h>

int main()
{
    int result;  // Declare an integer variable to store user input

    // Prompt the user to enter an integer number
    printf("Enter integer number:  ");
    scanf("%i", &result);

    // Evaluate the input using a switch statement
    switch (result) {
        case 1:
            // If the input is 1, print the value of the variable
            printf("Variable %i", result);
            break;

        case 245:
            // If the input is 245, print a specific message
            printf("Variable is 245\n");
            break;

        case 3:
            // If the input is 3, print a positive message
            printf("Good choice!!!\n");
            break;

        case 5:
            // If the input is 5, print an excellent message
            printf("Excellent result!!!\n");
            break;

        default:
            // If the input is any other number, print a default message
            printf("Some other number!");
    }

    // Print a new line for better output formatting
    printf("\n");

    // Return 0 to indicate the program ended successfully
    return 0;
}
