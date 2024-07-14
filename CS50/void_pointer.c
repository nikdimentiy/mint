/**
 * @file main.c
 * @brief Demonstrates the use of a void pointer to point to different data types.
 *
 * This program declares variables of type int, float, and char. It uses a void pointer
 * to point to these variables and prints their values by typecasting the void pointer.
 */

#include <stdio.h>

int main() {
    // Declare variables of different types
    int x = 33;
    float y = 12.4;
    char c = 'a';
    void *ptr;

    // Point the void pointer to the integer variable and print its value
    ptr = &x;
    printf("void ptr points to %d\n", *((int*)ptr));

    // Point the void pointer to the float variable and print its value
    ptr = &y;
    printf("void ptr points to %f\n", *((float *)ptr));

    // Point the void pointer to the char variable and print its value
    ptr = &c;
    printf("void ptr points to %c\n", *((char *)ptr));

    return 0;
}
