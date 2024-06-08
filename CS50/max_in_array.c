#include <stdio.h>

/**
 * @brief Finds the maximum element in an array and its index.
 *
 * This program prompts the user to enter the number of elements in an array,
 * followed by the elements themselves. It then finds the maximum element in
 * the array and its index, and prints these values to the console.
 *
 * @return int Returns 0 upon successful execution.
 */
int main()
{
    int array[100];  // Array to hold up to 100 integers
    int size;        // Number of elements in the array
    int c;           // Loop counter
    int location = 0; // Index of the maximum element

    // Prompt the user to enter the number of elements in the array
    printf("Enter the number of elements in array: ");
    scanf("%d", &size);

    // Check if the size is within the valid range
    if (size < 1 || size > 100) {
        printf("Invalid size. Please enter a number between 1 and 100.\n");
        return 1; // Exit the program with an error code
    }

    // Prompt the user to enter the elements of the array
    printf("Enter %d integers:\n", size);

    // Read the elements into the array
    for (c = 0; c < size; c++)
    {
        scanf("%d", &array[c]);
    }

    // Find the index of the maximum element in the array
    for (c = 1; c < size; c++)
    {
        if (array[c] > array[location])
        {
            location = c;
        }
    }

    // Print the maximum element and its index
    printf("The maximum element in the entered array is: %d and its index is %d.\n", array[location], location);

    return 0; // Return 0 to indicate successful execution
}
