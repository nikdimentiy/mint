#include <stdio.h>

/**
 * @brief Main function to find and print the divisors of a positive integer.
 * 
 * This program prompts the user to enter a positive integer.
 * It then calculates and prints all the divisors of the entered number.
 * Finally, it prints the total count of these divisors.
 * 
 * @return int Returns 0 on successful completion.
 */
int main()
{
    printf("Enter a positive integer number, please: \n");
    int n = 0;
    scanf("%d", &n);

    // Ensure the user enters a positive integer
    if (n <= 0) {
        printf("Invalid input! Please enter a positive integer.\n");
        return 1; // Exit with an error code
    }

    int count = 0;

    // Loop to find and print all divisors of n
    for(int i = 1; i <= n; i++)
    {
        if (n % i == 0) {
            count++;
            printf("The divisor of the entered number is: %d\n", i);
        }
    }

    // Print the total count of divisors
    printf("\n");
    printf("The total number of divisors of the entered number is: %d\n", count);

    return 0;
}
