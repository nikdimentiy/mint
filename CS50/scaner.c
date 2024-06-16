#include <stdio.h>
#include <limits.h>  // for INT_MAX, INT_MIN, LONG_MAX, LONG_MIN

/**
 * A simple C program to demonstrate basic input/output operations and data types.
 * It prompts the user for a character and two integers, performs basic arithmetic operations,
 * and prints information about integer data types and their sizes.
 */
int main() {
    printf("Enter any one keyboard character: \n");

    // Declare variables
    unsigned char letter;
    int a, b, c;

    // Input a character from user
    scanf("%c", &letter);

    // Prompt for two integers
    printf("Give me two integers separated by a space: \n");
    scanf("%d %d", &a, &b);

    // Perform arithmetic operations
    c = a + b;
    int d = a * b;

    // Output results
    printf("Result of operations:\n");
    printf("Sum of entered numbers: %d\n", c);
    printf("Product of entered numbers: %d\n", d);
    printf("\n");

    // Print the entered character and its memory address
    printf("Letter input: %c\n", letter);
    printf("Stored at memory: %p\n", (void *)&letter);
    printf("\n");

    // Print limits of integer data types
    printf("Max value of (Integer) data types:\n");
    printf("INT_MAX: %d\n", INT_MAX);
    printf("INT_MIN: %d\n", INT_MIN);
    printf("LONG_MAX: %ld\n", LONG_MAX);
    printf("LONG_MIN: %ld\n", LONG_MIN);
    printf("\n");

    // Print sizes of various data types
    printf("Size of data types:\n");
    printf("char \tsize: %lu bytes\n", sizeof(char));
    printf("float \tsize: %lu bytes\n", sizeof(float));
    printf("double \tsize: %lu bytes\n", sizeof(double));

    return 0;
}
