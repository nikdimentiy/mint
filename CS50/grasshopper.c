#include <stdio.h>

/**
 * Calculates the number of trajectories for a grasshopper to reach the nth point.
 * The grasshopper can jump 1 or 2 steps at a time.
 *
 * @param n The point the grasshopper wants to reach.
 * @return The number of different trajectories to reach point n.
 */
int number_of_trajectories(int n)
{
    int K[n+1]; // Array to store the number of trajectories to each point
    K[0] = 0;   // Base case: No way to reach point 0
    K[1] = 1;   // Base case: Only one way to reach point 1 (direct jump)
    
    // Calculate number of trajectories for each point from 2 to n
    for (int i = 2; i <= n; ++i)
        K[i] = K[i-1] + K[i-2];
    
    return K[n];
}

int main(int argc, char* argv[])
{
    int finish;
    printf("Enter the point the grasshopper wants to reach: ");
    scanf("%d", &finish); // Read the target point from the user
    
    // Print the number of trajectories from point 1 to the target point
    printf("Grasshopper has %d trajectories from 1 to %d\n",
           number_of_trajectories(finish), finish);
    
    return 0;
}
