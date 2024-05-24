/**
 * @file temperature_conversion.c
 * @brief This program generates a temperature conversion table from Fahrenheit to Celsius.
 *
 * The program prompts the user to enter the step value for the temperature increments,
 * and then it displays the corresponding Celsius values for Fahrenheit temperatures
 * starting from 0 up to 120 in the specified step increments.
 */

#include <stdio.h>

/**
 * @brief Main function to generate a temperature conversion table.
 *
 * This function reads the step value from the user, initializes the lower and upper
 * bounds for the Fahrenheit values, and then calculates and prints the corresponding
 * Celsius values for each step from the lower to the upper bound.
 *
 * @return int Returns 0 upon successful execution.
 */
int main(void)
{
    // Declare variables for Fahrenheit and Celsius temperatures, and step value
    int fahr, celsius;
    int lower, upper, step;

    // Prompt user to enter the step value for temperature increments
    printf("Enter the required step to represent the temperatures: \n");
    scanf("%i", &step);

    // Initialize the lower and upper bounds for Fahrenheit values
    lower = 0;   // Lower bound of the temperature table
    upper = 120; // Upper bound of the temperature table

    // Initialize Fahrenheit to the lower bound
    fahr = lower;

    // Loop to calculate and print the Celsius value for each Fahrenheit value
    while (fahr <= upper)
    {
        // Convert Fahrenheit to Celsius using the formula
        celsius = 5 * (fahr - 32) / 9;

        // Print the Fahrenheit and corresponding Celsius values
        printf("Fahrenheit value: %i\t Value in Celsius: %i\n", fahr, celsius);

        // Increment Fahrenheit by the step value
        fahr = fahr + step;
    }

    // Return 0 to indicate successful execution
    return 0;
}
