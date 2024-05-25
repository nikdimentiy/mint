#include <stdio.h>

/**
 * main - Entry point for the temperature conversion program
 *
 * Description:
 * This program prints a temperature conversion table from Fahrenheit to Celsius.
 * The table starts at 0 degrees Fahrenheit and ends at 110 degrees Fahrenheit,
 * with a step increment of 1 degree. The conversion formula used is:
 *   Celsius = (5.0 / 9.0) * (Fahrenheit - 32)
 *
 * Return: 0 on success
 */
int main(void)
{
    // Variable declarations
    float fahr, celsius;
    int lower, upper, step;

    // Initialize variables
    lower = 0;   // Lower limit of the temperature table
    upper = 110; // Upper limit of the temperature table
    step = 1;    // Step size

    // Set initial temperature to the lower limit
    fahr = lower;

    // Print the header of the table
    printf("Temperature Conversion Table (Fahrenheit to Celsius)\n");

    // Loop through the temperatures from lower to upper limits
    while (fahr <= upper)
    {
        // Convert Fahrenheit to Celsius
        celsius = 5.0 * (fahr - 32) / 9.0;

        // Print the current Fahrenheit and corresponding Celsius temperature
        printf("%3.0f %6.1f\n", fahr, celsius);

        // Increment the Fahrenheit temperature by the step size
        fahr = fahr + step;
    }

    return 0; // Indicate successful execution
}
