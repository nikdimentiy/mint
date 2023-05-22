// LeetCode task: solution -> https://leetcode.com/problems/longest-common-prefix/

package main

import (
	"fmt"
	"strings"
)

// longestCommonPrefix returns the longest common prefix among a slice of strings.
// It returns an empty string if the slice is empty or there is no common prefix.
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 { // if the slice is empty
		return "" // return an empty string
	}
	prefix := strs[0] // initialize prefix as the first string in the slice
	for i := 1; i < len(strs); i++ { // loop through the rest of the strings in the slice
		for !strings.HasPrefix(strs[i], prefix) { // while prefix is not a prefix of the current string
			prefix = prefix[:len(prefix)-1] // remove the last character from prefix
			if len(prefix) == 0 { // if prefix becomes empty
				return "" // return an empty string
			}
		}
	}
	return prefix // return the final prefix
}

func main() {
	strs := []string{"flower", "flow", "flight"} // a sample slice of strings
	result := longestCommonPrefix(strs) // call the function with the sample slice
	fmt.Println(result) // print the result to standard output
	// Output: fl
}
