#include <stdio.h>

/**
 * @brief Finds and prints multiples of a given number in a specified range.
 *
 * This program prompts the user to enter a start range, end range, and a number
 * to determine the multiplicity. It then finds and prints all numbers within
 * the range that are multiples of the specified number and counts them.
 *
 * @return 0 on successful execution.
 */
int main(void) {
    int start, end, multiple;
    int count = 0;

    // Prompt the user for the start of the range.
    printf("Enter any positive integer number (start range): \n");
    scanf("%i", &start);

    // Prompt the user for the end of the range.
    printf("Enter any positive integer number (finish range): \n");
    scanf("%i", &end);

    // Prompt the user for the number that determines multiplicity.
    printf("Enter the number, that determines multiplicity: ");
    scanf("%i", &multiple);

    printf("\n");

    // Iterate over the range and find multiples of the given number.
    for (int i = start; i <= end; i++) {
        if (i % multiple == 0) {
            printf("This number: %i - meets the specified conditions!\n", i);
            count++;
        }
    }

    printf("\n");
    // Print the total count of numbers that meet the conditions.
    printf("Total of numbers meeting the specified conditions in the given segment is: %i\n", count);

    return 0;
}
