// finding divisors of an entered number
#include <stdio.h>

int main(void) {
    int n, count;
    printf("Give me integer number: \n");
    scanf("%d", &n);

    count = 0;

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            printf("Divisor of entered number = %d\n", i);
            count++;
        }
    }
    printf("Total divisors of entered number = ");
    printf("%d\n", count);

    return 0;
}