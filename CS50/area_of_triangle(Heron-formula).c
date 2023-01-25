// code calculate: area of triangle (Heron's formula)

#include <stdio.h>
#include <math.h>

int main(void)
{
    double a, b, c, half_of_perimetr;

    printf("Enter the lenght of first cathetus: \n");
    scanf("%lf", &a);
    printf("Enter the lenght of second cathetus: \n");
    scanf("%lf", &b);
    printf("Enter the lenght ofthird cathetus: \n");
    scanf("%lf", &c);

    half_of_perimetr = (a + b + c) / 2;

    double p1 = half_of_perimetr - a;
    double p2 = half_of_perimetr - b;
    double p3 = half_of_perimetr - c;

    double S = sqrt(half_of_perimetr * (p1) * (p2) * (p3));

    printf("The area of a triangle is: %.2lf", S);

    return 0;
}
