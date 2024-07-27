#include <stdio.h>
#include <stdlib.h>

// Function to print a 2D dynamic array
void dynamic_array_print(int **A, size_t N, size_t M)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            // Printing each element with a width of 5 characters
            printf("%*d", 5, A[i][j]);
        }
        printf("\n");
    }
}

// Function to allocate memory for a 2D dynamic array
int **dynamic_array_alloc(size_t N, size_t M)
{
    int **A = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++)
    {
        A[i] = (int *)malloc(M * sizeof(int));
    }
    return A;
}

// Function to free memory allocated for a 2D dynamic array
void dynamic_array_free(int **A, size_t N)
{
    for (int i = 0; i < N; i++)
    {
        free(A[i]);
    }
    free(A);
}

// Function to test dynamic array allocation, initialization, and printing
void dynamic_array_test(size_t N, size_t M)
{
    int **A = dynamic_array_alloc(N, M);
    int x = 1;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            A[i][j] = x;
            x += 1;
        }
    }
    dynamic_array_print(A, N, M);

    // Memory investigation
    printf("\n Pointers to lines: ");
    for (int **p = A; p < A + N; p++)
        printf("%10d", (long int)*p);
    printf("\n Direct memory access:\n");
    for (int *p = (int *)*A; p < (int *)*A + N * M; p++)
        printf("%d\t", *p);

    dynamic_array_free(A, N);
}

int main()
{
    int matrix_height = 4;
    int matrix_width = 5;

    dynamic_array_test(matrix_height, matrix_width);
    return 0;
}
