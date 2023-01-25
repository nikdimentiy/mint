// this code calculates and represents the temperature conversion table: Fahrenheit to Celsius
#include <stdio.h>

int main(void)
{
  int fahr;
  for (fahr = 110; fahr >= 0; fahr--)
      printf("%3d %6.1f\n",fahr, (5.0/9) * (fahr - 32));
  return 0;
}

