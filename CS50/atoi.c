#include <stdio.h>
#include <stdlib.h>

/**
 * This program takes a number as input from the user and prints it.
 */

int main(int argc, char const *argv[]) {
  char input[10];
  int num;

  printf("Enter a number, please: \n");
  fgets(input, 10, stdin); // Read user input as a string
  num = atoi(input); // Convert the string to an integer
  printf("You entered number: %d\n", num);

  return 0;
}
