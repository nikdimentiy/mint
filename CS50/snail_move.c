#include <stdio.h>

/**
 * This program calculates the number of days required for a climber to reach 
 * a certain height when given the climbing speed during the day and the 
 * sliding speed during the night. The program takes three inputs from the user: 
 * the required height, the climbing speed, and the sliding speed. It ensures 
 * that the climbing speed is greater than the sliding speed for the calculations 
 * to be valid.
 */

int main(void) {
    int h, a, b;

    // Prompt user for the required segment length
    printf("Enter the length of the required segment: \n");
    scanf("%i", &h);

    // Prompt user for the climbing speed
    printf("Enter up speed: \n");
    scanf("%i", &a);

    // Prompt user for the sliding speed
    printf("Enter down speed: \n");
    scanf("%i", &b);

    // Ensure that the climbing speed is greater than the sliding speed
    if (a > b) {
        int count = 1; // Initialize day count
        int point = 0; // Current height

        // Loop until the current height plus climbing speed reaches or exceeds the required height
        while (point + a < h) {
            point = (point + a) - b; // Calculate new height after sliding down
            count++; // Increment day count
        }

        // Print the total number of days required
        printf("%i\n", count);

        return 0; // Successful execution
    } else {
        // Print an error message if the climbing speed is not greater than the sliding speed
        printf("You entered the wrong values!\n");
        return 1; // Indicate an error
    }
}
