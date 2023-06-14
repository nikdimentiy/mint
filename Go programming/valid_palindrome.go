// LeetCode task: solution -> https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
// Preparation to coding interview 🎯

package main

import (
	"fmt"
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	// Convert to lowercase and remove non-alphanumeric characters
	reg := regexp.MustCompile("[^a-zA-Z0-9]")
	s = strings.ToLower(reg.ReplaceAllString(s, ""))
	
	// Compare with the reversed string
	return s == reverseString(s)
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	s1 := "A man, a plan, a canal: Panama"
	fmt.Println(isPalindrome(s1))  // Output: true
	
	s2 := "race a car"
	fmt.Println(isPalindrome(s2))  // Output: false
}
