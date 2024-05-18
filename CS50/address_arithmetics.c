#include <stdio.h>

/**
 * This program demonstrates basic pointer arithmetic and comparisons in C.
 * 
 * It initializes an array of integers, prints specific elements using pointer
 * dereferencing and arithmetic, and compares two pointers to show the relative 
 * positioning of elements in the array.
 */

int main(int argc, char *argv[])
{
    // Initialize an array of 10 integers
    int A[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Print the first element of the array using pointer dereferencing
    printf("%d\n", *A);

    // Define a pointer that points to the 6th element of the array (index 5)
    int *p = A + 5;
    // Print the element before the one p is pointing to (5th element, index 4)
    printf("%d\n", p[-1]);

    // Define another pointer that points to the 8th element of the array (index 7)
    int *q = A + 7;
    // Compare the two pointers and print the result
    if (p > q)
        printf("p > q\n");
    else
        printf("p <= q\n");

    // Print the difference between the two pointers (in terms of array elements)
    printf("p - q = %d\n", p - q);

    return 0;
}
