#include <stdio.h>

/*
    This program prompts the user to input a string and then prints the entered string.
    It demonstrates the usage of fgets() function to safely read input strings from the user.
*/

int main()
{
    char buffer[50]; // Declare a character array to store the input string
    printf("Give me a string, please: \n"); // Prompt the user for input
    fgets(buffer, 35, stdin); // Read input string from the user with a maximum length of 35 characters

    // Print the input string as a confirmation
    printf("Thank you for the %s!\n", buffer);

    return 0; // Indicate successful completion of the program
}
