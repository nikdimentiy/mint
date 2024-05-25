#include <stdio.h>
#include <stdbool.h>
#include <iso646.h>

/**
 * main - Entry point for the number counting program
 *
 * Description:
 * This program reads integer inputs from the user and counts the occurrences
 * of numbers between 0 and 9. The input terminates when the user enters 10.
 * The program then prints each number in the range 0-9 the number of times
 * it was entered, separated by spaces.
 *
 * Return: 0 on success
 */
int main(int argc, char *argv[])
{
    // Initialize an array to count occurrences of numbers 0-9
    int counters[10] = {0};
    int x;

    // Continuously read input until the terminator (10) is encountered
    while (true)
    {
        // Read an integer from the user
        scanf("%d", &x);

        // If the input is 10, break the loop (terminate input)
        if (x == 10)
            break;

        // If the input is not in the range 0-9, continue to the next iteration
        if (x < 0 or x > 9)
            continue;

        // Increment the counter for the input number
        counters[x] += 1;
    }

    // Print the counted numbers
    for (x = 0; x < 10; ++x)
    {
        // Print each number the number of times it was counted
        for (int i = 0; i < counters[x]; ++i)
            printf("%3d ", x);
    }

    // Print a newline for better output formatting
    printf("\n");

    return 0; // Indicate successful execution
}
