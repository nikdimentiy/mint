# LeetCode task: solution -> https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
# 🎯 150 coding task: preparation to coding interview 🍀

package main

import (
	"strings"
)

type Solution struct{}

func (s *Solution) LengthOfLastWord(str string) int {
	// Trim leading and trailing spaces
	str = strings.TrimSpace(str)

	// Split the trimmed string into a slice of words
	words := strings.Split(str, " ")

	if len(words) > 0 {
		return len(words[len(words)-1])
	} else {
		return 0
	}
}

func main() {
	// Create an instance of the Solution struct
	solution := Solution{}

	// Call the LengthOfLastWord() method
	println(solution.LengthOfLastWord("Hello World"))                       // Output: 5
	println(solution.LengthOfLastWord("   fly me   to   the moon  "))       // Output: 4
	println(solution.LengthOfLastWord("luffy is still joyboy"))             // Output: 6
	println(solution.LengthOfLastWord("A singleword"))                      // Output: 9
	println(solution.LengthOfLastWord("  Spaces  "))                         // Output: 6
	println(solution.LengthOfLastWord(""))                                   // Output: 0
	println(solution.LengthOfLastWord("       "))                            // Output: 0
	println(solution.LengthOfLastWord("Symbol: ★"))                          // Output: 1
	println(solution.LengthOfLastWord("1234567890"))                         // Output: 10
	println(solution.LengthOfLastWord("This string has multiple last words")) // Output: 5
}

