#include <stdio.h>

/**
 * Solves the Tower of Hanoi puzzle.
 *
 * This function prints the steps required to move `n` disks from pin `i` to pin `k`
 * using a temporary pin. The Tower of Hanoi is a classic problem in which you have
 * three pins and a number of disks of different sizes that can slide onto any pin.
 * The puzzle starts with the disks neatly stacked in ascending order of size on one pin,
 * the smallest at the top, making a conical shape. The objective of the puzzle is to move
 * the entire stack to another pin, obeying the following simple rules:
 * 
 * 1. Only one disk can be moved at a time.
 * 2. Each move consists of taking the upper disk from one of the stacks and placing it on top
 *    of another stack or on an empty pin.
 * 3. No larger disk may be placed on top of a smaller disk.
 *
 * @param n The number of disks.
 * @param i The starting pin (source pin).
 * @param k The target pin (destination pin).
 */
void hanoi(int n, int i, int k);

int main(int argc, char* argv[])
{
    // Solves the Tower of Hanoi puzzle for 3 disks
    // moving from pin 1 to pin 2
    hanoi(3, 1, 2);

    return 0;
}

/**
 * Recursive function to solve the Tower of Hanoi puzzle.
 *
 * @param n The number of disks.
 * @param i The starting pin (source pin).
 * @param k The target pin (destination pin).
 */
void hanoi(int n, int i, int k)
{
    if (n == 1)
    {
        // Base case: Move a single disk directly from the source pin to the destination pin
        printf("Move disk 1 from pin %d to %d.\n", i, k);
    }
    else
    {
        // Determine the temporary pin (the pin that is not the source or destination)
        int tmp = 6 - i - k;

        // Move the top n-1 disks from the source pin to the temporary pin
        hanoi(n-1, i, tmp);

        // Move the nth disk from the source pin to the destination pin
        printf("Move disk %d from pin %d to %d.\n", n, i, k);

        // Move the n-1 disks from the temporary pin to the destination pin
        hanoi(n-1, tmp, k);
    }
}
