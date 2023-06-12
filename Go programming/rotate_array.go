// LeetCode task: solution -> https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
// Coding interview preparation 

package main

import (
	"fmt"
)

type Solution struct{}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	k := 3

	fmt.Println("Original Array:", nums)
	Solution{}.rotate(nums, k)
	fmt.Println("Rotated Array:", nums)
}

func (s Solution) rotate(nums []int, k int) {
	// Calculate the effective number of rotations
	k = k % len(nums)

	// Reverse the entire array
	s.reverse(nums, 0, len(nums)-1)

	// Reverse the first k elements
	s.reverse(nums, 0, k-1)

	// Reverse the remaining elements
	s.reverse(nums, k, len(nums)-1)
}

func (s Solution) reverse(nums []int, start int, end int) {
	for start < end {
		// Swap the elements at start and end indices
		nums[start], nums[end] = nums[end], nums[start]
		// Increment the start index and decrement the end index
		start++
		end--
	}
}
