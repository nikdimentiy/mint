// new version of popular code: possibility of processing in a loop
#include <stdio.h>

int main(void) {
    float new_price, old_price, q_dif;
    float growth_percentage;
    int number_of_shares;
    printf("Enter the number of shares: \n");
    scanf("%i", &number_of_shares);
    int N = number_of_shares;
    int count = 0;
    printf("\n");

    while (count < N)
    {
        printf("Enter today's stock price on stock market: \n");
        scanf("%f", &new_price);

        printf("Enter old stock price on stock market: \n");
        scanf("%f", &old_price);

        q_dif = new_price - old_price;
        growth_percentage = (q_dif / old_price) * 100;
        float result = growth_percentage;

        if (result > 0)
            printf("The share price increased by %3.3f percent\n", result);
        else
            printf("The stock lost %3.3f percentage in value\n", result);

        count++;
    }

    return 0;
}
