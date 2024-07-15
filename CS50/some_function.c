#include <stdio.h>

/**
 * @brief Displays the given number formatted to two decimal places.
 *
 * @param number The number to be displayed.
 */
void show_number(float number) {
    printf("Your number is %.2f\n", number);
}

/**
 * @brief Divides two numbers and returns the result. If the divisor is zero,
 *        returns zero to avoid division by zero.
 *
 * @param a The dividend.
 * @param b The divisor.
 * @return The result of the division, or zero if the divisor is zero.
 */
float divide(float a, float b) {
    float res;
    if (b != 0)
        res = a / b;
    else
        res = 0; // Return zero if the divisor is zero
    return res;
}

int main() {
    int num_1, num_2;

    // Prompt the user to enter the first number
    printf("Enter first number: \n");
    scanf("%i", &num_1);

    // Prompt the user to enter the second number
    printf("Enter second number: \n");
    scanf("%i", &num_2);

    // Perform the division and store the result
    float result = divide(num_1, num_2);

    // Display the result
    show_number(result);

    return 0;
}
