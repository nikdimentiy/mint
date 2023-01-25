#include <stdio.h>
#define N 21

int main()
{
    int sieve[N] = {0};

    for(int i = 2; i*i < N; ++i)
    {
        if (sieve[i] == 0)
        {
            for(int k = i*i; k < N; k += i)
            {
                sieve[k] = 1; // prime number - assignment 0, composite - assignment - 1
            }
        }

    }

    for (int i = 0; i < N; ++i)
    {
        printf("%4i", i); // output trivial line of numbers
    }

    printf("\n");

    for (int i = 0; i < N; ++i)
    {
        printf("%4i", sieve[i]); // the output line of algo finding prime numbers ([0], [1])
    }
    printf("\n");
    return 0;
}
