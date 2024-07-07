/**
 * This program concatenates two strings without using the strcat() function.
 * The first string is "programming is " and the second string is "awesome".
 * The program appends the second string to the first string and then prints the result.
 */

#include <stdio.h>

int main()
{
    // Declare and initialize two strings
    char str_1[] = "programming is ";
    char str_2[] = "awesome";

    // Variable to keep track of the length of str_1
    int length = 0;
    int j;

    // Calculate the length of str_1
    while (str_1[length] != '\0')
    {
        length++;
    }

    // Append str_2 to str_1
    for (j = 0; str_2[j] != '\0'; j++, length++)
    {
        str_1[length] = str_2[j];
    }

    // Null-terminate the resulting string
    str_1[length] = '\0';

    // Print the concatenated string
    printf("After concatenation --> the string is: %s\n", str_1);

    return 0;
}
