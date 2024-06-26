#include <stdio.h>
#include <string.h>

// Define a structure for a course
typedef struct {
    int id;                 // Course ID
    char title[40];         // Title of the course (up to 39 characters)
    float hours;            // Duration of the course in hours
} course;

int main() {
    course cs1;             // Declare variable for first course
    course cs2;             // Declare variable for second course

    // Initialize details for cs1
    cs1.id = 123456;
    strcpy(cs1.title, "JavaScript Basics");
    cs1.hours = 12.30;

    // Initialize details for cs2
    cs2.id = 341281;
    strcpy(cs2.title, "Advanced C++");
    cs2.hours = 14.25;

    // Display course information
    printf("Course ID\tTitle\t\t\t\tHours\n");
    printf("%d\t\t%s\t\t%4.2f\n", cs1.id, cs1.title, cs1.hours);
    printf("%d\t\t%s\t\t%4.2f\n", cs2.id, cs2.title, cs2.hours);

    return 0;
}
