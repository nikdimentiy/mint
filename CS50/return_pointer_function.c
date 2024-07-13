#include <stdio.h>

// Function prototype for get_evens
int* get_evens();

int main() {
    int *a;
    int k;

    // Call get_evens function to get the first 5 even numbers
    a = get_evens();
    
    // Print the first 5 even numbers
    for (k = 0; k < 5; k++)
        printf("%d\n", a[k]); 

    return 0;
}

// Function to generate the first 5 even numbers
int* get_evens() {
    static int nums[5]; // Static array to store the even numbers
    int k;
    int even = 0;

    // Generate and store the first 5 even numbers in the array
    for (k = 0; k < 5; k++) {
        nums[k] = even += 2;
    }

    return nums; // Return the array of even numbers
}
