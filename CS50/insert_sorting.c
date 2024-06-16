#include <stdio.h>
#include <stdbool.h>   // for bool, true, false
#include <iso646.h>    // for alternative logical operators (or, and)

#define ALLOCATE_SIZE 1000

/**
 * A program to demonstrate insertion sort on an array of integers.
 * It prompts the user to enter integers, sorts them using insertion sort,
 * and then prints the sorted array.
 */

// Function to input numbers into array A, stopping at 0 or max_size
int input_array(int A[], int max_size)
{
    int top = 0;

    while (true)
    {
        int x;
        scanf("%d", &x);
        
        // Stop input on encountering 0 or when max_size is reached
        if (x == 0 or top == max_size)
            break;
        
        A[top] = x;
        top++;
    }
    return top;  // Return the number of elements entered
}

// Function to print elements of array A up to index N-1
void print_array(int A[], int N)
{
    for (int i = 0; i < N; ++i)
        printf("%3d ", A[i]);
    printf("\n");
}

// Function to perform insertion sort on array A with N elements
void insert_sort(int A[], int N)
{
    for (int i = 1; i < N; ++i)
    {
        int k = i;
        // Perform insertion sort
        while (k > 0 and A[k - 1] > A[k])
        {
            // Swap elements if out of order
            int tmp = A[k - 1];
            A[k - 1] = A[k];
            A[k] = tmp;
            k -= 1;
        }
    }
}

// Main function
int main(int argc, char *argv[])
{
    printf("Enter numbers:");
    int A[ALLOCATE_SIZE];
    int N;

    // Input numbers into array A and get the count N
    N = input_array(A, ALLOCATE_SIZE);
    
    // Sort the array using insertion sort
    insert_sort(A, N);
    
    // Print the sorted array
    print_array(A, N);

    return 0;
}
