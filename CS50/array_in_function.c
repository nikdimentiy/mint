#include <stdio.h>

// Function prototype
int add_up(int A[], int num_elements);

/**
 * @brief Main function to calculate the sum of array elements.
 * 
 * This program defines an array of integers representing orders,
 * calls the add_up function to compute the total sum of the elements,
 * and then prints the result.
 * 
 * @return int Returns 0 on successful execution.
 */
int main() {
    // Define an array of integers representing orders
    int orders[5] = {100, 220, 37, 16, 98};

    // Call add_up function and print the total orders
    printf("Total orders is %d\n", add_up(orders, 5)); 

    return 0; // Return success code 0
}

/**
 * @brief Adds up the elements of an integer array.
 * 
 * This function takes an array of integers and its size as input,
 * iterates through the array, and returns the sum of its elements.
 * 
 * @param A Array of integers.
 * @param num_elements Number of elements in the array.
 * @return int The total sum of the array elements.
 */
int add_up(int A[], int num_elements) {
   // Initialize total to 0
   int total = 0;
   
   // Loop counter variable
   int k;

   // Loop through each element of the array
   for (k = 0; k < num_elements; k++) {
        // Add the current element to the total
        total += A[k];
   }

   // Return the total sum
   return total;
}
