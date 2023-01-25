// computer make the secret  number, user tries to guess it using four attempts
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iso646.h>

int main(void)
{
    printf("I am a very smart computer and I have a secret  number!\n");
    printf("You have 4 attempts - to guess it! The guessed number in the range from 1 to 99\n");

    int guess = 0;
    int attempt = 0;
    srand(time(NULL));
    int r_number = (1 + rand() % 99);

    printf("Your first attempt: \n");
    scanf("%i", &guess);
    while (guess != r_number  and attempt < 3)
    {
        if (guess < r_number)
            printf("This is less than planned number!\n");
        else if (guess > r_number)
            printf("This is more than planned number!\n");

        attempt +=1;
        printf("Try again! Your attempt: ");
        scanf("%i", &guess);
    }

    if (guess == r_number)
        printf("Awesome! You guessed it! Congratulations! \n");
    else
        printf("The attempts are over! You will be lucky next time!\n");
        printf("\n");
        printf("The secret number is %i\n", r_number);

    return 0;
}
