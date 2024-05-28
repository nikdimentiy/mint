#include <stdio.h>
#include <stdlib.h>

/**
 * @brief Main function to demonstrate memory allocation in a loop.
 * 
 * This program allocates a large array of integers multiple times in a loop.
 * If memory allocation fails, it exits with an error message. 
 * Otherwise, it initializes the array and prints a success message.
 * 
 * @param argc Number of command-line arguments.
 * @param argv Array of command-line arguments.
 * @return int Returns 0 on successful completion, 1 on memory allocation failure.
 */
int main(int argc, char* argv[])
{
    int N = 50000000; // Number of integers in the array

    // Loop to allocate and initialize memory multiple times
    for (int k = 0; k < 1000; ++k)
    {
        // Allocate memory for the array
        int *A = (int *)malloc(N * sizeof(int));
        if (NULL == A) {
            // If memory allocation fails, print an error message and exit
            printf("OS didn't give memory. Exit...\n");
            exit(1);
        }
        printf("Allocate array - OK. iteration %d.\n", k);

        // Initialize the array with values
        for (int i = 0; i < N; ++i)
            A[i] = i;

        // Free the allocated memory to prevent memory leaks
        free(A);
    }

    printf("Program is on finish!\n");

    // Pause the program before exiting (useful for Windows, can be commented out in Unix-like systems)
    system("pause");

    return 0;
}
