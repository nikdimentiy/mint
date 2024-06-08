#include <stdio.h>

/**
 * @brief Prompts the user for an integer input and ensures it is within the specified range (0 to 23).
 * 
 * @return int The validated height input from the user.
 */
int check_int(void);

/**
 * @brief Generates and prints a pyramid of the given height and peak width.
 * 
 * @param height The height of the pyramid.
 * @param peak The initial width of the pyramid's peak.
 */
void gen_pyramid(int height, int peak);

int main(void)
{
    int peak = 2;  // Initial width of the pyramid's peak
    int height = check_int();  // Get the validated height from the user
    gen_pyramid(height, peak);  // Generate and print the pyramid
}

int check_int(void)
{
    int i;
    // Prompt the user until a valid input (0 to 23) is received
    do
    {
        printf("Enter the height of the pyramid (0 to 23): \n");
        scanf("%i", &i);
    }
    while (i < 0 || i > 23);
    return i;
}

void gen_pyramid(int height, int peak)
{
    char air = ' ';  // Character used for spaces
    char block = '#';  // Character used for blocks

    // Loop through each row of the pyramid
    for (int r = 0; r < height; r++)
    {
        // Print the spaces before the blocks
        for (int a = 0; a < height - r - 1; a++)
        {
            printf("%c", air);
        }
        // Print the blocks in the current row
        for (int b = 0; b < peak + r; b++)
        {
            printf("%c", block);
        }
        printf("\n");  // Move to the next line after printing each row
    }
}
