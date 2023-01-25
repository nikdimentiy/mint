#include <stdio.h>

// get a positive integer from a user

int GetPositiveInt(void)
{
    int n;
    do 
    {
        printf("Please give me a positive integer number:");
        scanf("%i", &n);
    }
    
    while (n < 1);
    return n;
}   


int main(void)
{
    int n = GetPositiveInt();
    printf("Thanks for the %i!\n", n);
}
