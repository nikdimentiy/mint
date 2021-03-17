#include <stdio.h>
#include <limits.h>

int main(){
    printf("Enter any one keyboard character: \n");
    unsigned char letter;
    scanf("%c", &letter);
    printf("Give me two integers number separated by a space: \n");
    int a, b, c;
    scanf("%d%d", &a, &b);

    c = a + b;
    int d = (a * b);

    printf("Result of operation: sum of entered numbers: %i, product of entered numbers: %i\n", c, d);
    printf("\n");
    printf("Letter input: %c\n", letter);
    printf("Stored at memory: %p\n", letter);
    printf("\n");
    printf("Max value of (Integer) data types is: %i\n", INT_MAX);
    printf("Min value of (Integer) data types is: %i\n", INT_MIN);

    printf("\n");
    printf("Max value of (Integer) data types is: %ld\n", LONG_MAX);
    printf("Min value of (Integer) data types is: %ld\n", LONG_MIN);

    printf("\n");
    printf("char \tsize: %lu bytes\n", sizeof(char));
    printf("float \tsize: %lu bytes\n", sizeof(float ));
    printf("double \tsize: %lu bytes\n", sizeof(double ));

    return 0;
}
