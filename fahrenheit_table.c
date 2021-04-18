#include <stdio.h>

int main(void)
{
    int fahr, celsius;
    int lower, upper, step;
    printf("Enter the required step to represent the temperatures: \n");
    scanf("%i", &step);

    lower = 0;
    upper = 120;

    fahr = lower;
    while (fahr <= upper)
    {
        celsius = 5 * (fahr - 32) / 9;
        printf("Fahrenheit value: %i\t Value in Celsius: %i\n", fahr, celsius);
        fahr = fahr + step;
    }
}
