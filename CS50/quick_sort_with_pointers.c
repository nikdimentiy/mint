/**
 * This program sorts an array of integers using the qsort() function from the standard library.
 * The array to be sorted is {52, 23, 56, 19, 4}.
 * The compare function is used as the comparison function for qsort.
 */

#include <stdio.h>
#include <stdlib.h>

// Function prototype for the comparison function used in qsort
int compare(const void *elem1, const void *elem2);

int main()
{
    // Declare and initialize the array to be sorted
    int arr[5] = {52, 23, 56, 19, 4};
    int num, width, i;

    // Calculate the number of elements in the array
    num = sizeof(arr) / sizeof(arr[0]);

    // Calculate the size of each element in the array
    width = sizeof(arr[0]);

    // Sort the array using qsort, passing the compare function as the comparison function
    qsort((void *)arr, num, width, compare);

    // Print the sorted array
    for (i = 0; i < 5; i++)
        printf("%d ", arr[i]);

    return 0;
}

/**
 * Comparison function used by qsort to sort integers.
 * @param elem1 - Pointer to the first element to compare.
 * @param elem2 - Pointer to the second element to compare.
 * @return -1 if the first element is less than the second, 1 if greater, and 0 if they are equal.
 */
int compare(const void *elem1, const void *elem2)
{
    if ((*(int *)elem1) == (*(int *)elem2))
        return 0;
    else if ((*(int *)elem1) < (*(int *)elem2))
        return -1;
    else
        return 1;
}
