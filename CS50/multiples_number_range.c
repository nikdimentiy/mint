// The program finds multiples of number in the range
#include <stdio.h>

int main(void) {
    int x, y, z;
    int count = 0;
    printf("Enter any positive integer number (start range): \n");
    scanf("%i", &x);

    printf("Enter any positive integer number (finish range): \n");
    scanf("%i", &y);

    printf("Enter the number, that determines multiplicity: ");
    scanf("%i", &z);

    printf("\n");

    for (int i = x; i <= y; i++) {
        if (i % z == 0) {
            printf("This number: %i - meets the specified conditions!\n", i);
            count++;
        }
    }
    printf("\n");
    printf("Total of even numbers on a given segment is: %i\n", count);

    return 0;
}