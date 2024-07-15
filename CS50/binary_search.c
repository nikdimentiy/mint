#include <stdio.h>

/**
 * @brief Performs binary search on a sorted array.
 *
 * This program takes an array of integers and a target value as input. It uses the binary search
 * algorithm to find the target value in the array. If the target is found, it prints the position
 * of the target value. If the target is not found, it indicates that the target is not present in
 * the array.
 *
 * @return int Always returns 0 to indicate successful execution.
 */

int main() {
    int c, first, last, middle, n, search, array[100];

    // Prompt the user to enter the number of elements in the array
    printf("Enter number of elements\n");
    scanf("%d", &n);

    // Prompt the user to enter the elements of the array
    printf("Enter %d integers\n", n);
    for (c = 0; c < n; c++)
        scanf("%d", &array[c]);

    // Prompt the user to enter the value to search for
    printf("Enter value to find\n");
    scanf("%d", &search);

    first = 0;
    last = n - 1;
    middle = (first + last) / 2;

    // Binary search algorithm
    while (first <= last) {
        // If the middle element is less than the search value, ignore the left half
        if (array[middle] < search)
            first = middle + 1;
        // If the middle element is the search value, print the result and exit
        else if (array[middle] == search) {
            printf("%d found at location %d.\n", search, middle + 1);
            break;
        }
        // If the middle element is greater than the search value, ignore the right half
        else
            last = middle - 1;

        // Update the middle index
        middle = (first + last) / 2;
    }
    // If the search value is not found in the array, print a message
    if (first > last)
        printf("Not found! %d isn't present in the list.\n", search);

    return 0;
}
