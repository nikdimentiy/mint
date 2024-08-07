#include <stdio.h>
#include <stdlib.h>

// Function to modify the value pointed to by p
void foo(int* p)
{
    printf("Got: *p = %d\n", *p);
    *p += 10;
    printf("Did: *p = %d\n", *p);
}

// Function to demonstrate returning a pointer to a local variable
int* bar()
{
    int y = 888;
    printf("y = %d\n", y);
    return &y;
}

int main(int argc, char* argv[])
{
    int x = 7;
    printf("x = %d\n", x);
    
    // Call foo function to modify x
    foo(&x);
    printf("x = %d\n", x);

    // Call bar function which returns a pointer to a local variable
    int *py = bar();
    printf("*py = %d\n", *py);

    return 0;
}
