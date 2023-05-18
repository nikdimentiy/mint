// Leetcode task: solution -> https://leetcode.com/problems/valid-parentheses/

package main

import "fmt"

func isValid(s string) bool {
	stack := []rune{} // Initialize an empty stack to track opening brackets
	brackets := map[rune]rune{'(': ')', '{': '}', '[': ']'} // Mapping of opening brackets to closing brackets

	for _, char := range s {
		if _, ok := brackets[char]; ok { // If the character is an opening bracket
			stack = append(stack, char) // Push it onto the stack
		} else if _, ok := brackets[char]; ok { // If the character is a closing bracket
			if len(stack) == 0 { // If the stack is empty, there is no corresponding opening bracket
				return false
			}
			openingBracket := stack[len(stack)-1] // Get the top element from the stack
			stack = stack[:len(stack)-1]          // Pop the top element from the stack
			if brackets[openingBracket] != char { // Check if the closing bracket matches the opening bracket
				return false
			}
		}
	}

	return len(stack) == 0 // If the stack is empty, all opening brackets were closed properly
}

func main() {
	fmt.Println(isValid("()"))       // Output: true
	fmt.Println(isValid("()[]{}"))   // Output: true
	fmt.Println(isValid("(]"))       // Output: false
}
