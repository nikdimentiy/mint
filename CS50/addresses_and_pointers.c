/**
 * @file pointer_example.c
 * @brief Demonstrates the usage of pointers and pointer dereferencing in C.
 *
 * This program illustrates how to manipulate an integer variable using
 * pointers to the integer, pointers to pointers, and even pointers to pointers
 * to pointers. It changes the value of an integer through different levels
 * of indirection and prints the value of the integer at each stage.
 */

#include <stdio.h>

int main(int argc, char *argv[])
{
    // Declare and initialize an integer variable
    int i = 10;
    
    // Declare a pointer to the integer variable and assign its address
    int *pi = &i;
    
    // Declare a pointer to the pointer of the integer variable and assign its address
    int **ppi = &pi;
    
    // Declare a pointer to the pointer to the pointer of the integer variable and assign its address
    int ***pppi = &ppi;

    // Print the initial value of the integer variable
    printf("%d\n", i);

    // Modify the value of the integer variable through the single pointer
    *pi = 20;
    printf("%d\n", i);

    // Modify the value of the integer variable through the double pointer
    **ppi = 30;
    printf("%d\n", i);

    // Modify the value of the integer variable through the triple pointer
    ***pppi = 40;
    printf("%d\n", i);

    return 0;
}
