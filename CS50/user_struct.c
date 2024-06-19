/**
 * This program defines a structure to represent a student with fields
 * for age, grade, and name. It then declares two student variables,
 * initializes them with specific values, and prints their information.
 */

#include <stdio.h>

// Define a structure to represent a student
struct student {
    int age;         // Age of the student
    int grade;       // Grade of the student
    char name[40];   // Name of the student
};

int main()
{
    // Declare two variables of type struct student
    struct student s1;
    struct student s2;

    // Initialize the first student variable
    s1.age = 19;
    s1.grade = 9;
    sprintf(s1.name, "John Bighimer");

    // Initialize the second student variable
    s2.age = 22;
    s2.grade = 10;
    sprintf(s2.name, "Batman Jokerson");

    // Print the information of the first student
    printf("Student: %s, Age: %d, Grade: %d\n", s1.name, s1.age, s1.grade);

    // Print the information of the second student
    printf("Student: %s, Age: %d, Grade: %d\n", s2.name, s2.age, s2.grade);

    // Return 0 to indicate the program ended successfully
    return 0;
}
