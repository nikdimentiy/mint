#include <stdio.h>

#define N 10  // Define the size of the array

/**
 * @brief The main function demonstrates array initialization and printing.
 * 
 * The function initializes an array of size N, fills it with values from 0 to N-1,
 * and then prints each element of the array on a new line.
 * 
 * @return int Returns 0 upon successful execution.
 */
int main(void)
{
    int A[N] = {0};  // Initialize the array with zeros

    // Fill the array with values from 0 to N-1
    for (int i = 0; i < N; ++i)
        A[i] = i;

    // Print each element of the array on a new line
    for (int i = 0; i < N; ++i)
        printf("%d\n", A[i]);

    return 0;  // Return 0 to indicate successful execution
}
