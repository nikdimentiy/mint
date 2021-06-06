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
                sieve[k] = 1;
            }
        }

    }

    for (int i = 0; i < N; ++i)
    {
        printf("%4i", i);
    }

    printf("\n");

    for (int i = 0; i < N; ++i)
    {
        printf("%4i", sieve[i]);
    }
    printf("\n");
    return 0;
}
