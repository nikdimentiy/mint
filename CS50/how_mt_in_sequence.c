#include <stdio.h>

/**
 * This program counts how many times a specified digit (k) occurs in a sequence of numbers from 1 to N, including N.
 * 
 * The user is prompted to input:
 * 1. A positive integer N, representing the range of the sequence.
 * 2. An integer k, representing the digit to count within the sequence.
 * 
 * The program then iterates through each number in the sequence, checking each digit of the number.
 * If a digit matches k, a counter is incremented.
 * 
 * Finally, the total count of occurrences of the digit k in the range from 1 to N is printed.
 */

int main(void)
{
    int n, count, i, j, k;
    count = 0;

    // Prompt the user to enter the range of the sequence
    printf("Enter positive integer number (the range of the sequence): \n");
    scanf("%d", &n);

    // Prompt the user to enter the digit to count
    printf("Enter the integer number (what number occurs in this sequence - how many times): \n");
    scanf("%i", &k);

    // Loop through each number in the sequence from N to 1
    for (int i = n; i >= 1; i--)
    {
        j = i;
        // Check each digit of the current number
        while (j != 0)
        {
            // If the digit matches k, increment the count
            if (j % 10 == k)
            {
                count++;
            }
            // Remove the last digit from the current number
            j = j / 10;
        }
    }

    // Print the total count of occurrences of the digit k
    printf("The total value of numbers in the range from 1 to %d, including the number '%i'  is equal to: %d\n", n, k, count);

    return 0;
}
