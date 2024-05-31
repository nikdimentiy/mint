/**
 * @file array_creation.c
 * @brief This program dynamically allocates an array of characters and initializes it.
 *
 * The program prompts the user to enter the size of the array. It then allocates
 * memory for the array and initializes each element with its index value. If the 
 * memory allocation fails, the program prints an error message and exits.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * @brief Main function to create and initialize an array.
 *
 * The function prompts the user for the size of the array, allocates the memory,
 * initializes the array, and then pauses to show the result.
 * 
 * @param argc Number of command-line arguments (unused).
 * @param argv Array of command-line arguments (unused).
 * @return int Exit status of the program.
 */
int main(int argc, char* argv[])
{
    int N;  // Variable to store the size of the array

    // Prompt the user to enter the size of the array
    printf("Enter size of array to create: ");
    scanf("%d", &N);

    // Allocate memory for the array
    char *A = (char *)malloc(N);
    
    // Check if memory allocation was successful
    if (NULL == A)
    {
        printf("OS didn't give memory. Exit...\n");
        exit(1);
    }

    // Initialize the array with index values
    for (int i = 0; i < N; ++i)
        A[i] = i;

    // Inform the user that the array was successfully created
    printf("Array A successfully created!\n");

    // Pause the system to allow the user to see the output (note: not portable)
    system("pause");

    // Free the allocated memory (good practice, even though the program exits immediately)
    free(A);

    return 0;
}
