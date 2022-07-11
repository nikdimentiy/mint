#include <stdio.h>
int main()
{
    int array[100], size, c, location = 0;

    printf("Enter the number of elements in array\n");
    scanf("%d", &size);

    printf("Enter %d integers\n", size);

    for (c = 0; c < size; c++)
        scanf("%d", &array[c]);

    for (c = 1; c < size; c++)
        if (array[c] > array[location])
            location = c;

    printf(
        "The maximum element in the entered array is: %d and its index is %d.\n",
        array[location], location);
    return 0;
}
