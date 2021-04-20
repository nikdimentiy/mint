// this code calculates and represents the temperature conversion table: Fahrenheit to Celsius
#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 1

int main(void)
{
    int fahr;
    for(fahr = LOWER; fahr <= UPPER; fahr += STEP) {
        printf("%3d \t %6.2lf\n", fahr, (5.0 / 9.0) * (fahr - 32));
    }
    return 0;
}
