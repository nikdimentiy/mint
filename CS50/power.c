#include <stdio.h>

// function prototype
int power(int m, int n);

/* test of power function */
int main() {
  int i;
  for (i = 0; i <= 10; i++) {
    printf("Power: %d\t  Result: %d\n", i, power(2, i));
  }

  return 0;
}

/* the function calculates the basis of the n - power */
int power(int base, int n) {
  int i, p;
  p = 1;
  for (i = 1; i <= n; i++) {
    p = p * base;
  }
  return p;
}
