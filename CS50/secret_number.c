#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iso646.h>

/**
 * @brief A number guessing game where the computer generates a random number
 * between 1 and 99, and the user has four attempts to guess it.
 *
 * The program gives feedback after each guess to help the user.
 */

int main(void)
{
    // Introduction messages to the user
    printf("I am a very smart computer and I have a secret number!\n");
    printf("You have 4 attempts to guess it! The guessed number is in the range from 1 to 99\n");

    // Initialize variables
    int guess = 0;
    int attempt = 0;

    // Seed the random number generator and generate a random number between 1 and 99
    srand(time(NULL));
    int r_number = (1 + rand() % 99);

    // Prompt the user for the first attempt
    printf("Your first attempt: \n");
    scanf("%i", &guess);

    // Loop until the user guesses correctly or runs out of attempts
    while (guess != r_number and attempt < 3)
    {
        // Provide feedback if the guess is too low or too high
        if (guess < r_number)
            printf("This is less than the planned number!\n");
        else if (guess > r_number)
            printf("This is more than the planned number!\n");

        // Increment the attempt counter
        attempt += 1;

        // Prompt the user for another guess
        printf("Try again! Your attempt: ");
        scanf("%i", &guess);
    }

    // Check if the user guessed correctly
    if (guess == r_number)
        printf("Awesome! You guessed it! Congratulations! \n");
    else
    {
        // Inform the user that attempts are over and reveal the secret number
        printf("The attempts are over! Better luck next time!\n");
        printf("\n");
        printf("The secret number was %i\n", r_number);
    }

    return 0;
}
