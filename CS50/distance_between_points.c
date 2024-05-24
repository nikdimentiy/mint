/**
 * @file distance_between_points.c
 * @brief This program calculates the distance between two points in a coordinate system.
 *
 * The program prompts the user to enter the coordinates of two points and then calculates
 * the Euclidean distance between these points using the distance formula.
 */

#include <stdio.h>
#include <math.h>

/**
 * @brief Main function to calculate the distance between two points.
 *
 * The function reads the coordinates of two points from the user, calculates the horizontal
 * and vertical distances, and then computes the Euclidean distance between the two points.
 * Finally, it prints the distance to the console.
 *
 * @return int Returns 0 upon successful execution.
 */
int main(void)
{
    // Declare variables to store coordinates of the points
    double x1, x2, y1, y2;
    double horizontal_distance, vertical_distance, distance_between_points;

    // Prompt user for the coordinates of the first point
    printf("Enter the coordinates of the first point: \n");
    printf("X1 = ");
    scanf("%lf", &x1);
    printf("Y1 = ");
    scanf("%lf", &y1);

    // Prompt user for the coordinates of the second point
    printf("Enter the coordinates of the second point: \n");
    printf("X2 = ");
    scanf("%lf", &x2);
    printf("Y2 = ");
    scanf("%lf", &y2);

    // Calculate the horizontal and vertical distances squared
    horizontal_distance = pow(x2 - x1, 2);
    vertical_distance = pow(y2 - y1, 2);

    // Calculate the Euclidean distance between the points
    distance_between_points = sqrt(horizontal_distance + vertical_distance);

    // Print the distance
    printf("Distance between the entered points is: %.2lf\n", distance_between_points);

    return 0;
}
