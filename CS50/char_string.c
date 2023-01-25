#include <stdio.h>

int main()
{
    char buffer[50];
    printf("Give me a string, please: \n");
    fgets(buffer, 35, stdin);
    printf("Thank you for the %s!\n", buffer);
    return 0;
}