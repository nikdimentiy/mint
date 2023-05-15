// This code implements the two sum algorithm.
//
// Given an array of integers nums and an integer target,
// find two numbers in nums such that their sum is equal to target.
//
// The algorithm works by first creating a hash map,
// where the keys are the integers in nums and the values are their indices.
// Then, it iterates through the array,
// and for each number num,
// it checks if the target - num is in the hash map.
// If it is,
// the algorithm returns the indices of the two numbers.
// Otherwise,
// it adds the number num to the hash map.
// If the algorithm reaches the end of the array without finding any two numbers whose sum is equal to target,
// it returns an empty list.

func twoSum(nums []int, target int) []int {
    // Create a hash map to store the indices of the integers in nums.
    hashMap := make(map[int]int)

    // Iterate through the array.
    for i, num := range nums {
        // Check if the target - num is in the hash map.
        if diff, ok := hashMap[target-num]; ok {
            // If it is, return the indices of the two numbers.
            return []int{i, diff}
        }

        // Otherwise, add the number num to the hash map.
        hashMap[num] = i
    }

    // If the algorithm reaches the end of the array without finding any two numbers whose sum is equal to target,
    // return an empty list.
    return []int{}
}

