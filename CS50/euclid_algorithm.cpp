/**
 * @file gcd_euclidean.cpp
 * @brief This program calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
 *
 * The Euclidean algorithm is based on the principle that the GCD of two numbers does not change if the larger number
 * is replaced by its remainder when divided by the smaller number. This process is repeated until one of the numbers
 * becomes zero, and the other number is the GCD.
 */

#include <iostream>
using namespace std;

/**
 * @brief Main function to calculate the GCD of two integers.
 *
 * The function prompts the user to enter two integers, then uses the Euclidean algorithm to find their GCD.
 * It prints debug statements to trace the intermediate steps and finally displays the GCD.
 * 
 * @return int Exit status of the program.
 */
int main()
{
    int64_t a;  // Variable to store the first integer
    int64_t b;  // Variable to store the second integer

    // Prompt the user to enter two integers
    cout << "Enter two integer numbers separated by space: " << endl;
    cin >> a >> b;

    // Euclidean algorithm to find the GCD
    while (a != 0 && b != 0) {
        if (a > b) {
            cout << "DEBUG: Case 1 -> a: " << a << " b: " << b << endl;
            a = a % b;  // Replace 'a' with its remainder when divided by 'b'
        } else {
            cout << "DEBUG: Case 2 -> a: " << a << " b: " << b << endl;
            b = b % a;  // Replace 'b' with its remainder when divided by 'a'
        }
    }

    // Output the GCD, which is the non-zero value of 'a' or 'b'
    cout << "The greatest common divisor is: " << (a + b) << endl;

    return 0;
}
