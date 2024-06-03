#include <stdio.h>

/**
 * This program continuously prompts the user to enter an integer number
 * and determines whether the entered number is even or odd. The process
 * terminates when the user inputs 0, and a message indicating the termination
 * is displayed.
 */

int main(void) {
    int x = 1; // Initialize x to a non-zero value to start the loop

    // Loop until the user inputs 0
    while (x != 0) {
        // Prompt the user to enter an integer number
        printf("Give me an integer number: \n");
        printf("To terminate the process of inputting numbers, please input 0 (zero): \n");
        
        // Read the user input
        scanf("%d", &x);
        
        // Check if the input number is even, odd, or zero
        if (x % 2 == 0 && x != 0) {
            // If the number is even and not zero, print that it is even
            printf("Your number %i is even!\n", x);
        } else if (x != 0) {
            // If the number is odd and not zero, print that it is odd
            printf("Your number %i is odd!\n", x);
        } else {
            // If the number is zero, print a termination message
            printf("You entered 0! Terminating the process.\n");
        }
    }

    return 0;
}
