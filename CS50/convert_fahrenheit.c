// Temperature conversion table (Farenheit to Celsius)

#include <stdio.h>

int main(void)
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 110;
    step = 1;

    fahr = lower;
    printf("Temperature conversion table (Farenheit to Celsius)\n");
    while (fahr <= upper)
    {
        celsius = 5.0 * (fahr - 32) / 9.0;
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
