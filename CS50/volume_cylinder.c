#include <stdio.h>
#include <math.h>

/**
 * This program computes the volume of a cylinder and a cone
 * based on user-provided height and radius values.
 */

int main(void) {
    // Declare variables for height, radius, and pi
    double height, radius;
    double pi = 3.14159265358979323846;

    // Prompt the user for the height of the cylinder or cone
    printf("Enter please - the needed height for (cylinder or cone): \n");
    scanf("%lf", &height);

    // Prompt the user for the radius of the figure
    printf("Enter please - needed radius of the figure: \n");
    scanf("%lf", &radius);

    // Calculate the square of the radius
    double square_radius = pow(radius, 2);

    // Calculate the volume of the cylinder
    double Volume_cylinder = height * pi * square_radius;

    // Calculate the volume of the cone
    double Volume_cone = (height * pi * square_radius) / 3;

    // Print the results
    printf("Result of operation: \n");
    printf("The volume of the cylinder is: %.2lf\n", Volume_cylinder);
    printf("The volume of the cone is: %.2lf\n", Volume_cone);

    return 0;
}
