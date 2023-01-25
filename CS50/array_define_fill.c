// array fill and print on the screen

#include <stdio.h>
#define N 10

int main(void)
{
    int A[N] = {0};

    for (int i = 0; i < N; ++i)
      A[i] = i;
      
    for(int i = 0; i < N; ++i)
      printf("%i\n", A[i]);

    return 0;
}
