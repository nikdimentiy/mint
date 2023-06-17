// LeetCode task: solution -> https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
// 🍀 Preparig for coding interview 🎯


package main

import "fmt"
 
func isSubsequence(s string, t string) bool {
	i, j := 0, 0
	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
		}
		j++
	}
	return i == len(s)
}

func main() {
	s := "abc"
	t := "ahbgdc"
	fmt.Println(isSubsequence(s, t))  // Output: true

	s = "axc"
	t = "ahbgdc"
	fmt.Println(isSubsequence(s, t))  // Output: false
}
