#include <stdio.h>

#define N 10

void print_array(int A[])
{
    for(int i = 0; i < N; ++i)
        printf(" %d ", A[i]);
    printf("\n");
}

int main(int argc, char* argv[])
{
    int A[N] = {0};

    for(int i = 0; i < N; ++i)  // Sample 1
        A[i] = i;
    print_array(A);

    for(int i = 0; i < N; ++i)  // Sample 2
        A[i] = N - 1 - i;
    print_array(A);

    for(int i = 0; i < N; ++i)  // Sample 3
        A[N - 1 - i] = i;
    print_array(A);

    for(int i = 0; i < N; ++i)  // Sample 4
        A[i] = i%2;
    print_array(A);

    for(int i = 0; i < N/2; ++i)  // Sample 5
    {
        A[2*i] = i;
        A[2*i+1] = N/2 + i;
    }
    print_array(A);

    return 0;
}
