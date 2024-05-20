#include <stdio.h>

/**
 * This program displays uppercase and lowercase letters in the ASCII table.
 * ASCII (American Standard Code for Information Interchange) is a character encoding
 * standard used for electronic communication. It represents text in computers,
 * telecommunications equipment, and other devices.
 */

int main(void)
{
    // Display uppercase letters
    for (int i = 65; i < 65 + 26; i++)
    {
        printf("%c: %i\n", (char) i, i);
    }

    printf("\n");

    // Display lowercase letters
    for (int i = 97; i < 97 + 26; i++)
    {
        printf("%c: %i\n", (char) i, i);
    }

    return 0;
}
