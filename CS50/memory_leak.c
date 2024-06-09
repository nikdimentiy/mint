#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * @brief Allocates memory and duplicates the array.
 *
 * This function allocates memory for a new array and copies the contents
 * of the input array to the newly allocated array. It is the caller's 
 * responsibility to free the allocated memory to avoid memory leaks.
 *
 * @param A The input array to duplicate.
 * @param N The number of elements in the input array.
 * @return A pointer to the newly allocated array containing the duplicate
 *         of the input array.
 */
int *duplicate_array(int *A, size_t N)
{
    // Allocate memory for the new array.
    int *B = (int *)malloc(sizeof(int) * N);
    if (B == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    // Copy elements from A to B.
    for (size_t i = 0; i < N; i++)
        B[i] = A[i];

    printf("duplicate_array() allocated memory for the duplicate.\n");
    return B;
}

int main()
{
    printf("Calling irresponsible function duplicate_array():\n");
    
    // Initialize an array of 10 integers.
    int A[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Call the function to duplicate the array.
    int *B = duplicate_array(A, 10);

    // Print the duplicated array.
    for (int i = 0; i < 10; ++i)
        printf("%d\t", B[i]);
    printf("\n");

    printf("Since caller function is not taking responsibility by itself,\n");
    printf("memory for the array above will never be released...\n\n");

    printf("The same situation for the standard function strdup():\n");
    
    // Duplicate a string using strdup.
    const char *hello = "Hello, World!";
    char *message = strdup(hello);
    if (message == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    printf("Strdup allocated memory for this message: \"%s\"\n", message);
    printf("It'll never be released...\n\n");

    // Example of improper memory management in a loop.
    int *p;
    for (int i = 0; i < 10; i++)
    {
        p = (int *)malloc(sizeof(int));
        if (p == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
        printf("Allocating memory many times in cycle.\n");
        *p = i;
    }
    free(p); // Only the last allocated memory is released.
    printf("But releasing it just once...\n");

    // Free allocated memory to prevent memory leaks.
    free(B);
    free(message);

    return 0;
}
