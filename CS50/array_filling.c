#include <stdio.h>

#define N 10  // Define the size of the array

/**
 * @brief Prints the elements of an array.
 * 
 * @param A An integer array of size N.
 */
void print_array(int A[])
{
    for(int i = 0; i < N; ++i)
        printf(" %d ", A[i]);
    printf("\n");
}

/**
 * @brief The main function demonstrates various array manipulations and prints the results.
 * 
 * The function initializes an array of size N and performs the following operations:
 * 1. Fills the array with values from 0 to N-1.
 * 2. Fills the array with values from N-1 to 0.
 * 3. Fills the array with values from 0 to N-1 but in reverse order.
 * 4. Fills the array with alternating 0s and 1s.
 * 5. Fills the array such that the first half contains indices 0 to N/2-1 and the second half contains N/2 to N-1.
 * 
 * @param argc Number of command-line arguments.
 * @param argv Array of command-line arguments.
 * @return int Returns 0 upon successful execution.
 */
int main(int argc, char* argv[])
{
    int A[N] = {0};  // Initialize array with zeros

    // Sample 1: Fill the array with values from 0 to N-1
    for(int i = 0; i < N; ++i)
        A[i] = i;
    print_array(A);

    // Sample 2: Fill the array with values from N-1 to 0
    for(int i = 0; i < N; ++i)
        A[i] = N - 1 - i;
    print_array(A);

    // Sample 3: Fill the array with values from 0 to N-1 in reverse order
    for(int i = 0; i < N; ++i)
        A[N - 1 - i] = i;
    print_array(A);

    // Sample 4: Fill the array with alternating 0s and 1s
    for(int i = 0; i < N; ++i)
        A[i] = i % 2;
    print_array(A);

    // Sample 5: Fill the array such that first half contains 0 to N/2-1 and second half contains N/2 to N-1
    for(int i = 0; i < N/2; ++i)
    {
        A[2*i] = i;
        A[2*i + 1] = N/2 + i;
    }
    print_array(A);

    return 0;
}
