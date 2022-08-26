#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  char input[10];
  int num;

  printf("Enter a number, please: \n");
  fgets(input, 10, stdin);
  num = atoi(input);
  printf("You entered number: %d\n", num);

  return 0;
}
