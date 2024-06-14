#include <stdio.h>

/**
 * This program demonstrates the use of pointers in C.
 * It initializes two integers, one of which is accessed via a pointer.
 * It then performs an arithmetic operation using the pointer and prints the results.
 */
int main() {
    // Initialize integer variables
    int z = 7;
    int j = 63;

    // Initialize a pointer variable that points to the address of 'j'
    int *p = &j;

    // Perform an arithmetic operation using the value pointed to by 'p' and 'z'
    int result = *p + z;

    // Print the address of 'j'
    printf("The address of j is %p\n", (void*)&j);

    // Print the address stored in the pointer 'p'
    printf("p contains address %p\n", (void*)p);

    // Print the value of 'j'
    printf("The value of j is %d\n", j);

    // Print the value pointed to by 'p'
    printf("p is pointing to the value %d\n", *p);

    // Print the result of the arithmetic operation
    printf("The new RESULT of operation with pointer is: %d\n", result);

    return 0;
}
