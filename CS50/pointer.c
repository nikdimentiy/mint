#include <stdio.h>

int main() {
    int z = 7;
    int j = 63;
    int *p = &j;

    int result = *p + z;

    printf("The address of j is %x\n", &j);
    printf("p contains address %x\n", p);
    printf("The value of j is %d\n", j);
    printf("p is pointing to the value %d\n", *p);
    printf("The new RESULT of operation with pointer is: %d\n",result);
}
