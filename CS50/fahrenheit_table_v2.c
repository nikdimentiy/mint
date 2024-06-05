#include <stdio.h>

#define LOWER 0   // Lower limit of the temperature table (in Fahrenheit)
#define UPPER 300 // Upper limit of the temperature table (in Fahrenheit)
#define STEP 1    // Step size for each increment in the temperature table (in Fahrenheit)

/**
 * @file temperature_conversion.c
 * @brief This program calculates and prints a temperature conversion table
 *        from Fahrenheit to Celsius.
 *
 * The table starts from LOWER limit (0 Fahrenheit) to UPPER limit (300 Fahrenheit)
 * with increments defined by STEP (1 Fahrenheit).
 *
 * The conversion formula used is:
 *     Celsius = (5.0 / 9.0) * (Fahrenheit - 32)
 */

int main(void)
{
    int fahr; // Variable to hold the temperature in Fahrenheit

    // Loop through the range of Fahrenheit temperatures
    for(fahr = LOWER; fahr <= UPPER; fahr += STEP) {
        // Print the Fahrenheit temperature and its corresponding Celsius value
        printf("%3d \t %6.2lf\n", fahr, (5.0 / 9.0) * (fahr - 32));
    }

    return 0; // Indicate that the program ended successfully
}
