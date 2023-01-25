#include <stdio.h>

int main(void) {
    int h, a, b;
    printf("Enter the length of the required segment: \n");
    scanf("%i", &h);

    printf("Enter up speed: \n");
    scanf("%i", &a);

    printf("Enter down speed: \n");
    scanf("%i", &b);

    if (a > b) {
        int count = 1;
        int point = 0;
        while (point + a < h) {
            point = (point + a) - b;
            {
                count++;
            }
        }

        printf("%i\n", count);

        return 0;
    } else {
        printf("You entered the wrong values!");
    }
}
