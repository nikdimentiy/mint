#include <stdio.h>

/**
 * @brief Main function to find and print the divisors of an entered integer.
 * 
 * This program prompts the user to enter an integer. It then calculates and
 * prints all the divisors of the entered number. Finally, it prints the total
 * count of these divisors.
 * 
 * @return int Returns 0 on successful completion.
 */
int main(void) {
    int n, count;

    // Prompt the user to enter an integer
    printf("Give me an integer number: \n");
    scanf("%d", &n);

    count = 0;

    // Loop to find and print all divisors of n
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            // If i is a divisor, print it and increment the count
            printf("Divisor of entered number = %d\n", i);
            count++;
        }
    }

    // Print the total number of divisors
    printf("Total divisors of entered number = %d\n", count);

    return 0;
}
