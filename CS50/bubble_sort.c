#include <stdio.h>

/**
 * bubble_sort - Sorts an array of integers in ascending order
 * using the Bubble Sort algorithm.
 * @a: Array of integers to be sorted.
 * @n: Number of elements in the array.
 *
 * This function repeatedly iterates through the array and
 * swaps adjacent elements if they are in the wrong order.
 * After each pass through the array, the next largest element
 * is placed in its correct position.
 */
void bubble_sort(int a[], int n) {
    int i, j, tmp;
    // Iterate over the entire array n times
    for (i = 0; i < n; i++) {
        // Iterate over the array up to the last sorted element
        for (j = 0; j < n - i - 1; j++) {
            // Swap if the current element is greater than the next
            if (a[j] > a[j + 1]) {
                tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }
}

int main() {
    int a[100], n, i;
    // Prompt the user to enter the number of elements in the array
    printf("Enter number of elements in the array:\n");
    scanf("%d", &n);

    // Validate the number of elements
    if (n <= 0 || n > 100) {
        printf("Invalid number of elements. Please enter a number between 1 and 100.\n");
        return 1;
    }

    // Prompt the user to enter the elements of the array
    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // Sort the array using bubble sort
    bubble_sort(a, n);

    // Print the sorted array
    printf("Printing the sorted array:\n");
    for (i = 0; i < n; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}
