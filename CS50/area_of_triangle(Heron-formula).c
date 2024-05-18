#include <stdio.h>
#include <math.h>

/**
 * This program calculates the area of a triangle using Heron's formula.
 * 
 * Heron's formula states that the area of a triangle whose sides have lengths 
 * a, b, and c is:
 * 
 * Area = sqrt(s * (s - a) * (s - b) * (s - c))
 * 
 * where s is the semi-perimeter of the triangle:
 * 
 * s = (a + b + c) / 2
 * 
 * The program prompts the user to input the lengths of the three sides of the triangle 
 * and then calculates and displays the area.
 */

int main(void)
{
    double a, b, c, half_of_perimeter, area;

    // Prompt the user to enter the length of the first side
    printf("Enter the length of the first side: \n");
    scanf("%lf", &a);

    // Prompt the user to enter the length of the second side
    printf("Enter the length of the second side: \n");
    scanf("%lf", &b);

    // Prompt the user to enter the length of the third side
    printf("Enter the length of the third side: \n");
    scanf("%lf", &c);

    // Calculate the semi-perimeter of the triangle
    half_of_perimeter = (a + b + c) / 2;

    // Calculate the area using Heron's formula
    area = sqrt(half_of_perimeter * (half_of_perimeter - a) * (half_of_perimeter - b) * (half_of_perimeter - c));

    // Display the area of the triangle
    printf("The area of the triangle is: %.2lf\n", area);

    return 0;
}
