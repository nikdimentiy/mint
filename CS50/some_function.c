#include <stdio.h>

void show_number(float number) {
    printf("Your number is %.2f\n", number);
}

float delete(float a, float b) {
    float res;
    if (b != 0)
        res = a / b;
    else
        res = 0;
    return res;

}

int main() {
    int num_1, num_2;
    printf("Enter first number: \n");
    scanf("%i", &num_1);

    printf("Enter second number: \n");
    scanf("%i", &num_2);

    float result = delete(num_1, num_2);
    show_number(result);


    return 0;
}
