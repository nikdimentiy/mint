// the code calculate: the distance between points in the coordinate system

#include <stdio.h>
#include <math.h>

int main(void)
{
    double x1,x2, y1,y2;
    double horizontal_distance, vertical_distance, distance_between_points;
    printf("Enter the coordinates of first point: \n");
    printf("X1 = ");
    scanf("%lf", &x1);
    printf("Y1 = ");
    scanf("%lf", &y1);

    printf("Enter the coordinates of second point: \n");
    printf("X2 = ");
    scanf("%lf", &x2);
    printf("Y2 = ");
    scanf("%lf", &y2);

    horizontal_distance = pow(x2 - x1, 2);
    vertical_distance = pow(y2 - y1, 2);
    distance_between_points = sqrt(horizontal_distance + vertical_distance);

    printf("Distance between entered points is: %.2lf\n", distance_between_points);
    return 0;
}
