#include <stdio.h>

int main()
{
    printf("Enter a  positive integer number, please: \n");
    int n = 0;
    scanf("%d", &n);
    int count = 0;

    for(int i = 2; i <= n; i++)
        {
            if (n % i == 0) {
            count++;
            printf("The divisor of entered number is: %d\n", i);
        }
        }
    printf("\n");
    printf("The total divisors of entered number is: %d\n", count);

    return 0;
}
