#include <stdio.h>

/**
 * @file circle_info.c
 * @brief This program defines structures for a point and a circle, 
 * initializes them, and prints the circle's radius and center coordinates.
 */

/**
 * @struct point
 * @brief A structure to represent a point in 2D space.
 * 
 * @var point::x
 * Member 'x' represents the x-coordinate of the point.
 * 
 * @var point::y
 * Member 'y' represents the y-coordinate of the point.
 */
typedef struct
{
    int x;
    int y;
} point;

/**
 * @struct circle
 * @brief A structure to represent a circle.
 * 
 * @var circle::radius
 * Member 'radius' represents the radius of the circle.
 * 
 * @var circle::center
 * Member 'center' represents the center of the circle as a point.
 */
typedef struct
{
    float radius;
    point center;
} circle;

/**
 * @brief Main function to initialize and print circle information.
 * 
 * Initializes a point and a circle, then prints the circle's radius 
 * and center coordinates.
 * 
 * @return int Returns 0 upon successful execution.
 */
int main()
{
    // Initialize a point with coordinates (3, 4)
    point p;
    p.x = 3;
    p.y = 4;

    // Initialize a circle with radius 3.14 and center at point p
    circle c;
    c.radius = 3.14;
    c.center = p;

    // Print the circle's radius and center coordinates
    printf("Circle radius is %.2f, center is at (%d, %d)\n", c.radius, c.center.x, c.center.y);

    return 0;
}
