#include <stdio.h>

/**
 * @file temperature_conversion.c
 * @brief This program calculates and prints a temperature conversion table
 *        from Fahrenheit to Celsius in descending order.
 *
 * The table starts from 110 Fahrenheit and goes down to 0 Fahrenheit,
 * decrementing by 1 Fahrenheit in each step.
 *
 * The conversion formula used is:
 *     Celsius = (5.0 / 9.0) * (Fahrenheit - 32)
 */

int main(void)
{
    int fahr; // Variable to hold the temperature in Fahrenheit

    // Loop through the range of Fahrenheit temperatures in descending order
    for (fahr = 110; fahr >= 0; fahr--) {
        // Print the Fahrenheit temperature and its corresponding Celsius value
        printf("%3d %6.1f\n", fahr, (5.0 / 9) * (fahr - 32));
    }

    return 0; // Indicate that the program ended successfully
}
