/**
 * @file array_operations.c
 * @brief Demonstrates various operations on an array in C.
 *
 * This program performs and demonstrates the following operations on an array:
 * 1. Print the array.
 * 2. Reverse the array.
 * 3. Cycle shift the array to the left.
 * 4. Cycle shift the array to the right.
 */

#include <stdio.h>

#define N 10 // Define the size of the array

/**
 * @brief Prints the elements of an array.
 * 
 * @param A The array to be printed.
 */
void print_array(int A[])
{
    // Loop through each element of the array and print it
    for (int i = 0; i < N; ++i)
        printf(" %d ", A[i]);
    printf("\n");
}

int main(int argc, char *argv[])
{
    // Initialize the array with values 0, 10, 20, ..., 90
    int A[N] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90};
    int tmp; // Temporary variable for swapping
    print_array(A); // Print the initial array

    // Reverse the array
    for (int i = 0; i < N / 2; ++i)
    {
        // Swap the ith element with the (N-1-i)th element
        tmp = A[i];
        A[i] = A[N - 1 - i];
        A[N - 1 - i] = tmp;
    }
    print_array(A); // Print the reversed array

    // Cycle shift the array to the left by one position
    tmp = A[0]; // Store the first element
    for (int i = 0; i < N - 1; ++i)
        A[i] = A[i + 1]; // Shift each element to the left
    A[N - 1] = tmp; // Move the first element to the last position
    print_array(A); // Print the array after left cycle shift

    // Cycle shift the array to the right by one position
    tmp = A[N - 1]; // Store the last element
    for (int i = N - 1; i > 0; --i)
        A[i] = A[i - 1]; // Shift each element to the right
    A[0] = tmp; // Move the last element to the first position
    print_array(A); // Print the array after right cycle shift

    return 0; // Return 0 to indicate successful execution
}
