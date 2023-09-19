package main

import (
	"fmt"
)

// main is the entry point of the program.
func main() {
	// Initialize a string containing "Hello Gophers!❤️"
	s := "Hello Gophers!❤️"
	// Print the original string
	fmt.Println(s)

	// Iterate over each rune in the string
	for _, runeValue := range s {
		// Print the rune and its type
		fmt.Printf("%v\t%T\n", string(runeValue), runeValue)

		// Convert the rune to bytes
		runeBytes := []byte(string(runeValue))

		// Iterate over each byte in the rune
		for _, byteValue := range runeBytes {
			// Print the original rune, the byte, and its integer value
			fmt.Printf("%v\t%T\t%d\n", string(runeValue), byteValue, byteValue)
		}
	}
}
