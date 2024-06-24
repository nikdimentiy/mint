#include <stdio.h>

/**
 * Program: Student Information Display
 * Author: [Your Name]
 * Description:
 * This program declares a structure to store student information including 
 * age, grade, and name. It then creates two student instances, initializes them
 * with specific values, and prints the students' names and ages.
 */

/* Define a structure to hold student information */
struct student {
    int age;       // Age of the student
    int grade;     // Grade of the student
    char name[40]; // Name of the student
};

int main() {
    /* Declare and initialize two student variables */
    struct student s1 = {19, 9, "John Birghimer"};
    struct student s2 = {22, 10, "Batman Jokerson"};

    /* Print the name and age of each student */
    printf("Student: %s, Age: %d, Grade: %d\n", s1.name, s1.age, s1.grade);
    printf("Student: %s, Age: %d, Grade: %d\n", s2.name, s2.age, s2.grade);

    return 0;
}
