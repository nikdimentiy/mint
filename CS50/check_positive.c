#include <stdio.h>

/*
    This program prompts the user to input a positive integer and then prints the entered number.
    It demonstrates a simple function to ensure that the user inputs a positive integer.
*/

// Function prototype
int GetPositiveInt();

int main(void)
{
    // Call GetPositiveInt() function to get a positive integer from the user
    int n = GetPositiveInt();
    
    // Print the entered positive integer as a confirmation
    printf("Thanks for the %i!\n", n);
}

// Function to get a positive integer from the user
int GetPositiveInt(void)
{
    int n;
    do
    {
        // Prompt the user to input a positive integer
        printf("Please give me a positive integer number: ");
        scanf("%i", &n);
    }
    // Continue prompting until a positive integer is entered
    while (n < 1);
    
    return n; // Return the positive integer entered by the user
}
