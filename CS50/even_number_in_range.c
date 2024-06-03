#include <stdio.h>

/**
 * This program prompts the user to input two positive integer numbers representing
 * a range (start and finish). It then iterates through this range and identifies 
 * and counts all even numbers within it. The program outputs each even number 
 * found and displays the total count of even numbers at the end.
 */

int main(void)
{
    int x, y;
    int count = 0;

    // Prompt user to enter the start of the range
    printf("Enter any positive integer number (start range): \n");
    scanf("%i", &x);

    // Prompt user to enter the end of the range
    printf("Enter any positive integer number (finish range): \n");
    scanf("%i", &y);
    
    printf("\n");

    // Loop through the range from x to y (inclusive)
    for(int i = x; i <= y; i++)
    {
        // Check if the current number is even
        if(i % 2 == 0)
        {
            // Print the even number
            printf("This number %i is even!\n", i);
            // Increment the count of even numbers
            count++;
        }
    }

    // Print a newline for better output formatting
    printf("\n");
    // Print the total count of even numbers found in the range
    printf("Total of even numbers in the given segment is: %i\n", count);

    return 0;
}
