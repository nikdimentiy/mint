#include <stdio.h>

int main(void) {
    int x = 1;

    while (x != 0) {
        printf("Give me integer number: \n");
        scanf("%d", &x);
        if (x % 2 == 0 && x != 0)
            printf("Your %i (number) is even!\n", x);
        else if (x != 0)
            printf("Your %i (number) is odd!\n", x);
        else
            printf("Your entered 0!\n");
    }
}
