#include <stdio.h>
#include <math.h>

/**
 * This program calculates the area of a triangle given the lengths of two sides (catheti)
 * and the angle between them in degrees. The formula used is:
 * 
 * Area = 0.5 * a * b * sin(C)
 * 
 * where:
 * a and b are the lengths of the two sides,
 * C is the angle between them.
 * 
 * The program converts the angle from degrees to radians before using the sine function.
 */

int main(int argc, char *argv[]) {
    double first_k, second_k, alpha_angle, area, alpha_radians;
    const double pi = 3.141593; // Define a constant for Pi

    // Prompt the user to enter the length of the first cathetus
    printf("Enter the length of the first cathetus: \n");
    scanf("%lf", &first_k);

    // Prompt the user to enter the length of the second cathetus
    printf("Enter the length of the second cathetus: \n");
    scanf("%lf", &second_k);

    // Prompt the user to enter the angle in degrees
    printf("Enter the angle value in degrees: \n");
    scanf("%lf", &alpha_angle);

    // Convert the angle from degrees to radians
    alpha_radians = alpha_angle * pi / 180;

    // Calculate the area of the triangle
    area = 0.5 * first_k * second_k * sin(alpha_radians);
    printf("The area of the triangle is: %.2lf\n", area);

    return 0;
}
