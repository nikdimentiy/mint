#include <stdio.h>

/**
 * @file convert_to_uppercase.c
 * @brief A simple program to convert a string to uppercase.
 *
 * This program prompts the user for a string input, converts all lowercase letters 
 * in the string to uppercase, and then prints the modified string.
 *
 * 
 * 1. The program declares a buffer to store the input string.
 * 2. It prompts the user to enter a string.
 * 3. It reads the input string using `fgets`.
 * 4. It iterates through the string and converts all lowercase letters to uppercase.
 * 5. Finally, it prints the modified string.
 *
 * @return 0 on successful execution.
 */

int main()
{
    // Declare a buffer to hold the input string with a size of 50 characters
    char buffer[50];

    // Prompt the user to enter a string
    printf("Give me a string, please: \n");

    // Read the input string from the user with a maximum length of 34 characters
    fgets(buffer, 35, stdin);

    // Iterate over each character in the buffer until the null terminator is reached
    for (int i = 0; buffer[i] != '\0'; i++) {
        // Check if the character is a lowercase letter
        if (buffer[i] >= 'a' && buffer[i] <= 'z') {
            // Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
            buffer[i] = buffer[i] - 32;
        }
    }

    // Print the modified string
    printf("Thank you for your string value! %s\n", buffer);

    // Return 0 to indicate successful execution
    return 0;
}
