#include <stdio.h>

// Function prototypes
int add(int num1, int num2);
int subtract(int num1, int num2);
int multiply(int num1, int num2);
int divide(int num1, int num2);

/**
 * @brief Main function to perform arithmetic operations based on user input.
 * 
 * This program prompts the user to enter two integers and then select an arithmetic
 * operation (add, subtract, multiply, or divide). It performs the selected operation
 * using function pointers and displays the result.
 * 
 * @return int Returns 0 on successful execution.
 */
int main() 
{
  // Declare variables for user input and result
  int x, y, choice, result;
  
  // Array of function pointers to store operations
  int (*op[4])(int, int);

  // Assign functions to the function pointer array
  op[0] = add;
  op[1] = subtract;
  op[2] = multiply;
  op[3] = divide;

  // Prompt the user to enter two integers
  printf("Enter two integers: ");
  scanf("%d%d", &x, &y);

  // Prompt the user to choose an operation
  printf("Enter 0 to add, 1 to subtract, 2 to multiply, or 3 to divide: ");
  scanf("%d", &choice);

  // Check if the choice is valid (0 to 3)
  if (choice < 0 || choice > 3) {
    printf("Invalid choice\n");
    return 1; // Return error code 1 for invalid choice
  }

  // Call the chosen function through the function pointer array
  result = op[choice](x, y);

  // Display the result of the operation
  printf("The result of operation is: %d\n", result);
    
  return 0; // Return success code 0
}

/**
 * @brief Adds two integers.
 * 
 * @param x First integer.
 * @param y Second integer.
 * @return int The sum of x and y.
 */
int add(int x, int y) {
  return x + y;
}

/**
 * @brief Subtracts the second integer from the first.
 * 
 * @param x First integer.
 * @param y Second integer.
 * @return int The difference between
