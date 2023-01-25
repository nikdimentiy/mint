// The code computes the  area of the cylinder and cone
#include <stdio.h>
#include <math.h>

int main(void) {
    double height, radius;
    double pi = 3.14159265358979323846;

    printf("Enter please - the needed height for (cylinder or cone): \n");
    scanf("%lf", &height);
    printf("Enter please - needed radius of the figure: \n");
    scanf("%lf", &radius);

    double square_radius = pow(radius, 2);
    double Volume_cylinder = (height * pi) * square_radius;
    double Volume_cone = ((height * pi) / 3) * square_radius;
    printf("Result of operation: \n");
    printf("The volume of the cylinder is:%.2lf\n", Volume_cylinder);
    printf("The volume of the cone is:%.2lf\n", Volume_cone);

    return 0;
}
