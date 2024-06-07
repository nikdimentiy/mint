#include <math.h>
#include <stdio.h>

/**
 * This program implements the insertion sort algorithm to sort an array of integers.
 *
 * Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
 * It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
 *
 * The program includes the following functions:
 * 1. insertionSort: Sorts an array using insertion sort.
 * 2. printArray: Prints the elements of an array.
 * 3. main: Driver function to test the insertion sort implementation.
 */

/* Function to sort an array using insertion sort */
void insertionSort(int arr[], int n)
{
    int i, key, j;

    // Loop through each element in the array starting from the second element
    for (i = 1; i < n; i++) {
        key = arr[i]; // Store the current element as the key
        j = i - 1;

        /* Move elements of arr[0..i-1], that are
           greater than key, to one position ahead
           of their current position */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]; // Shift element to the right
            j = j - 1; // Move to the previous element
        }
        arr[j + 1] = key; // Insert the key at the correct position
    }
}

/* A utility function to print an array of size n */
void printArray(int arr[], int n)
{
    int i;

    // Loop through each element in the array and print it
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n"); // Print a newline character at the end
}

/* Driver program to test insertion sort */
int main()
{
    // Initialize an array of integers to be sorted
    int arr[] = { 12, 11, 13, 5, 6 };
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    // Sort the array using insertion sort
    insertionSort(arr, n);

    // Print the sorted array
    printArray(arr, n);

    return 0; // Indicate successful program termination
}
