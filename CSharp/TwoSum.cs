using System;

// Declare a class named Program
class Program
{
    // Declare a static method named Main that takes no parameters and returns nothing
    static void Main()
    {
        // Create an instance of the TwoSum class and assign it to a variable named solver
        TwoSum solver = new TwoSum();

        // Create an array of integers and assign it to a variable named nums
        int[] nums = new int[] { 2, 7, 11, 15 };

        // Declare an integer and assign it to a variable named target
        int target = 9;

        // Call the TwoSum method on the solver object with nums and target as arguments and assign the result to a variable named result
        int[] result = solver.TwoSum(nums, target);

        // Print the result array to the console using the Join method of the String class
        Console.WriteLine("[" + String.Join(", ", result) + "]");
    }
}

// Declare a class named TwoSum
class TwoSum
{
    // Declare a method that takes an array of integers and a target integer as parameters and returns an array of two indices that add up to the target
    public int[] TwoSum(int[] nums, int target)
    {
        // Create a dictionary to store the indices of the integers in nums as values and the integers themselves as keys
        Dictionary<int, int> hashMap = new Dictionary<int, int>();

        // Iterate through the array using a for loop with a variable i as the index
        for (int i = 0; i < nums.Length; i++)
        {
            // Assign the integer at index i to a variable num
            int num = nums[i];

            // Check if the target - num is in the hash map using the ContainsKey method
            if (hashMap.ContainsKey(target - num))
            {
                // If it is, return an array with two elements: i and the value associated with target - num in the hash map
                return new int[] { i, hashMap[target - num] };
            }

            // Otherwise, add a new entry to the hash map with num as the key and i as the value using the Add method
            hashMap[num] = i;
        }

        // If the algorithm reaches the end of the array without finding any two numbers whose sum is equal to target,
        // return an empty array using the new keyword
        return new int[] { };
    }
}
