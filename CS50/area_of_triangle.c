#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {
    double first_k, second_k, alpha_angle, area, alpha_degrees, pi = 3.141593;

    printf("Enter the length of the first cathetus: \n");
    scanf("%lf", &first_k);

    printf("Enter the lenght of the second cathetus: \n");
    scanf("%lf", &second_k);

    printf("Enter angle value: \n");
    scanf("%lf", &alpha_angle);

    alpha_degrees = alpha_angle * pi / 180;

    area = ((first_k * second_k) * (sin)(alpha_degrees));
    printf("The area of the triangle is: %3.2lf", area / 2);

    return 0;
}
