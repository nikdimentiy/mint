#include <stdio.h>

/*
    This program demonstrates the usage of the sprintf function to format a string with dynamic values.
    It creates a message about the number of employees in a specific department.
*/

int main()
{
    char info[100]; // Initialize a character array to store the formatted information
    char dept[] = "HR"; // Define the department name
    int emp = 75; // Define the number of employees in the department

    // Format the information using sprintf to include the department name and number of employees
    sprintf(info, "The %s dept has %d employees.", dept, emp);

    // Uncomment the line below to print the formatted information
    // printf("%s\n", info);

    return 0;
}
