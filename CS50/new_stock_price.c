/**
 * @file stock_price_calculator.c
 * @brief A program to calculate the percentage change in stock prices.
 *
 * This program calculates the percentage change in stock prices based on the 
 * old price and the new price provided by the user for a given number of shares.
 */

#include <stdio.h>

/**
 * @brief Main function to execute the stock price change calculation.
 * 
 * This function prompts the user to enter the number of shares and then iteratively
 * asks for the new and old prices of each share. It calculates the percentage change
 * in price and displays whether the share price increased or decreased.
 * 
 * @return int Returns 0 upon successful execution.
 */
int main(void) {
    float new_price, old_price, q_dif;
    float growth_percentage;
    int number_of_shares;

    // Prompt user to enter the number of shares
    printf("Enter the number of shares: \n");
    scanf("%i", &number_of_shares);

    int N = number_of_shares; // Total number of shares to process
    int count = 0; // Counter to keep track of processed shares
    printf("\n");

    // Loop through each share to calculate and display the price change
    while (count < N) {
        // Prompt user to enter the new price of the stock
        printf("Enter today's stock price on stock market: \n");
        scanf("%f", &new_price);

        // Prompt user to enter the old price of the stock
        printf("Enter old stock price on stock market: \n");
        scanf("%f", &old_price);

        // Calculate the difference and the growth percentage
        q_dif = new_price - old_price;
        growth_percentage = (q_dif / old_price) * 100;

        // Determine if the price increased or decreased and display the result
        if (growth_percentage > 0) {
            printf("The share price increased by %3.3f percent\n", growth_percentage);
        } else {
            printf("The stock lost %3.3f percentage in value\n", growth_percentage);
        }

        count++; // Increment the counter
    }

    return 0; // Indicate successful execution
}
