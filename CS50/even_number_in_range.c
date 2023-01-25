#include <stdio.h>

int main(void)
{
    int x, y;
    int count = 0;
    printf("Enter any positive integer number (start range): \n");
    scanf("%i", &x);

    printf("Enter any positive integer number (finish range): \n");
    scanf("%i", &y);
    
    printf("\n");

    for(int i  = x; i <= y; i++)
    {
        if(i % 2 == 0)
        {
            printf("This number  %i is even!\n", i);
            count++;
        }
    }
    printf("\n");
    printf("Total of even numbers on a given segment is: %i", count);

    return 0;
}
