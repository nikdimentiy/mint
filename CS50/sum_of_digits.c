// C program to compute sum of digits in number

/* Function to get sum of digits */
int getSum(int n) 
{ 
    int sum = 0; 
    while (n != 0) 
{ 
    sum = sum + n % 10; 
    n = n/10; 
} 
    return sum; 
} 

# include <stdio.h> 
int main() 
{
    int n;
    printf("Enter integer number: \n");
    scanf("%d", &n);

    printf("The sum of digits, of entered number is: ");
    printf("%d\n",getSum(n)); 
    return 0; 
}

