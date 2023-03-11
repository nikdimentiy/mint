// the code draws a pyramid of a given height

#include <stdio.h>

int check_int(void);
void gen_pyramid(int h, int p);

int main(void)
{
    int peak = 2;
    int height = check_int();
    gen_pyramid(height, peak);
}

int check_int(void)
{
    int i;
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
    char air = ' ';
    char block = '#';
    for (int r = 0; r < height; r++)
    {
        for (int a = 0; a < height - r - 1 ; a++)
        {
            printf("%c", air);
        }
        for (int b = 0; b < peak + r; b++)
        {
            printf("%c", block);
        }
        printf("\n");
    }
}