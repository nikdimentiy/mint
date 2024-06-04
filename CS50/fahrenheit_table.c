#include <stdio.h>

/**
 * Main function to convert a range of Fahrenheit temperatures to Celsius.
 *
 * This program prompts the user to enter a step value for representing the temperatures.
 * It then converts temperatures from Fahrenheit to Celsius in steps from the lower bound (0) 
 * to the upper bound (120) and prints the results.
 */
int main(void) {
    int fahr, celsius;  // Variables to store Fahrenheit and Celsius values
    int lower, upper, step;  // Variables for the lower bound, upper bound, and step size

    // Prompt the user to enter the step value for temperature conversion
    printf("Enter the required step to represent the temperatures: \n");
    scanf("%i", &step);

    lower = 0;  // Set the lower bound of the temperature range
    upper = 120;  // Set the upper bound of the temperature range

    fahr = lower;  // Initialize fahr to the lower bound
    while (fahr <= upper) {
        celsius = 5 * (fahr - 32) / 9;  // Convert Fahrenheit to Celsius
        printf("Fahrenheit value: %i\t Value in Celsius: %i\n", fahr, celsius);  // Print the conversion result
        fahr = fahr + step;  // Increment fahr by the step value
    }

    return 0;  // Return 0 to indicate successful execution
}
