#include <stdio.h>

/*
    This program calculates the percentage change in stock prices based on user input.
    It takes the number of shares and compares the new and old stock prices to determine the percentage change.
*/

int main(void) {
    float new_price, old_price, q_dif;
    float growth_percentage;
    int number_of_shares;

    // Ask the user to input the number of shares
    printf("Enter the number of shares: \n");
    scanf("%i", &number_of_shares);
    int N = number_of_shares;
    int count = 0;
    printf("\n");

    // Loop through each share to calculate the percentage change
    while (count < N)
    {
        // Ask the user to input today's stock price
        printf("Enter today's stock price on the stock market: \n");
        scanf("%f", &new_price);

        // Ask the user to input the old stock price
        printf("Enter the old stock price on the stock market: \n");
        scanf("%f", &old_price);

        // Calculate the price difference and growth percentage
        q_dif = new_price - old_price;
        growth_percentage = (q_dif / old_price) * 100;
        float result = growth_percentage;

        // Display the result based on the percentage change
        if (result > 0)
            printf("The share price increased by %3.3f percent\n", result);
        else
            printf("The stock lost %3.3f percentage in value\n", result);

        count++;
    }

    return 0;
}
