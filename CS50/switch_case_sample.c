#include <stdio.h>

int main()
{
    int result;
    printf("Enter integer number:  ");
    scanf ("%i", &result);

    switch (result) {
        case 1:
        printf("Variable %i", result);
        break;

        case 245:
        printf("Variable is 245\n");
        break;

        case 3:
        printf("Good choise!!!\n");
        break;

        case 5:
        printf("Exelent result!!!\n");
        break;

        default:
        printf("Some other number!");
    }
    printf("\n");

    return 0;
}
