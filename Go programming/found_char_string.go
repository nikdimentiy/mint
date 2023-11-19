// Go code
package main

import (
	"fmt"
	"strings"
)

/**
 * This program prompts the user to enter a string, then checks if the string starts with 'i', ends with 'n', and contains 'a'.
 * The program is case-insensitive and prints "Found!" if the conditions are met, and "Not Found!" otherwise.
 */
func main() {
	// Prompt the user to enter a string
	fmt.Print("Enter a string: ")
	// Declare a variable to store the string
	var str string
	// Read the string from the standard input
	fmt.Scanln(&str)
	// Convert the string to lower-case
	str = strings.ToLower(str)
	// Check if the string starts with 'i', ends with 'n', and contains 'a'
	if strings.HasPrefix(str, "i") && strings.HasSuffix(str, "n") && strings.Contains(str, "a") {
		// Print "Found!" if the condition is true
		fmt.Println("Found!")
	} else {
		// Print "Not Found!" otherwise
		fmt.Println("Not Found!")
	}
}
