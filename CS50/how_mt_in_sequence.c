// the mini-program count how many times the number 7 occurs in a sequence of numbers from 1 to N, including N
#include <stdio.h>

int main(void)
{
    int n, count, i, j, k;
    count = 0;
    printf("Enter positive integer number (the range of the sequence): \n");
    scanf("%d",&n);

    printf("Enter the integer number (what number occurs in this sequence - how many times): \n");
    scanf("%i", &k);

    for (int i = n; i >= 1; i--)
    {
        j = i;
        while (j != 0 )
        {
            if (j % 10 == k)
            {
                count++;
            }
            j = j/10;
        }
    }
    printf("The total value of numbers in the range from 1 to %d, including the number '%i'  is equal to: %d\n", n, k, count);

    return 0;
}