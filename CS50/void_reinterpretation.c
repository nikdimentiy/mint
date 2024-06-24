#include <stdio.h>
#include <stdlib.h>

/**
 * Program: Abstract Data Type Printer
 * Author: [Your Name]
 * Description:
 * This program demonstrates how to use a void pointer to handle different
 * data types. It defines a function, `print_abstract`, which prints the value
 * of the data pointed to by the void pointer based on the type marker passed.
 * The `main` function initializes different types of variables, assigns their
 * addresses to a void pointer, and calls `print_abstract` to print their values.
 */

/* Function prototype for print_abstract */
void print_abstract(void *p, int type_marker);

int main(int argc, char *argv[])
{
    /* Declare and initialize variables of different types */
    char c = 'W';
    int i = 450;
    double d = -1;

    /* Declare a void pointer */
    void *p;

    /* Assign the address of the char variable to the void pointer and print */
    p = &c;
    print_abstract(p, 1);

    /* Assign the address of the int variable to the void pointer and print */
    p = &i;
    print_abstract(p, 2);

    /* Assign the address of the double variable to the void pointer and print */
    p = &d;
    print_abstract(p, 3);

    return 0;
}

/**
 * Function: print_abstract
 * ------------------------
 * Prints the value pointed to by the void pointer based on the type marker.
 *
 * p:          void pointer to the data
 * type_marker: integer indicating the type of data
 *              (1 for char, 2 for int, 3 for double)
 */
void print_abstract(void *p, int type_marker)
{
    if (type_marker == 1)
        printf("%c\n", *(char *)p);   // Print char value
    else if (type_marker == 2)
        printf("%d\n", *(int *)p);    // Print int value
    else if (type_marker == 3)
        printf("%lf\n", *(double *)p); // Print double value
    else
    {
        printf("Unknown type marker. Exiting.\n");
        exit(1);  // Exit the program if the type marker is unknown
    }
}
