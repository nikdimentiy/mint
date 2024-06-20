#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/**
 * @brief Demonstrates potential causes of segmentation faults in C.
 *
 * This program contains examples of common mistakes that can lead to
 * segmentation faults, such as dereferencing uninitialized pointers
 * and improper use of the `scanf` function.
 */

/**
 * @brief Sets the value pointed to by the given pointer to 0.
 *
 * @param pointer A pointer to an integer. Must not be NULL.
 */
void foo(int *pointer)
{
    assert(pointer);  // Ensure the pointer is not NULL
    *pointer = 0; // Potential segmentation fault if pointer is NULL
}

int main()
{
    // Uncommenting the following lines will cause segmentation faults

    // Example of an uninitialized pointer leading to a segmentation fault
    // int *p = NULL;  // Uninitialized pointer!
    // *p = 10; // Using it => Segmentation fault!

    // Example of passing an uninitialized pointer to a function
    // foo(p);  // Another use of uninitialized pointer => Segmentation fault!

    // Correctly initializing a pointer to an integer
    int x = 100;

    // Example of improper use of `scanf` leading to a segmentation fault
    // Correct usage: `scanf("%d", &x);`
    scanf("%d", &x); // Potential segmentation fault if the address of x is not passed

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/**
 * @brief Demonstrates potential causes of segmentation faults in C.
 *
 * This program contains examples of common mistakes that can lead to
 * segmentation faults, such as dereferencing uninitialized pointers
 * and improper use of the `scanf` function.
 */

/**
 * @brief Sets the value pointed to by the given pointer to 0.
 *
 * @param pointer A pointer to an integer. Must not be NULL.
 */
void foo(int *pointer)
{
    assert(pointer);  // Ensure the pointer is not NULL
    *pointer = 0; // Potential segmentation fault if pointer is NULL
}

int main()
{
    // Uncommenting the following lines will cause segmentation faults

    // Example of an uninitialized pointer leading to a segmentation fault
    // int *p = NULL;  // Uninitialized pointer!
    // *p = 10; // Using it => Segmentation fault!

    // Example of passing an uninitialized pointer to a function
    // foo(p);  // Another use of uninitialized pointer => Segmentation fault!

    // Correctly initializing a pointer to an integer
    int x = 100;

    // Example of improper use of `scanf` leading to a segmentation fault
    // Correct usage: `scanf("%d", &x);`
    scanf("%d", &x); // Potential segmentation fault if the address of x is not passed

    return 0;
}
