package main

import "fmt"

func romanToInt(s string) int {
	// Create a map to map symbols to values
	values := map[rune]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

	// Initialize variables to keep track of previous symbol and result
	var prev rune
	var result int

	// Iterate through the string of symbols
	for _, symbol := range s {
		// Get the value of the current symbol
		value := values[symbol]

		// If the previous symbol is not zero and its value is less than the current symbol's value,
		// subtract its value from the current symbol's value and add the difference to the result
		if prev != 0 && values[prev] < value {
			result += value - 2*values[prev]
			// Otherwise, just add the value of the current symbol to the result
		} else {
			result += value
		}

		// Set the current symbol as the previous symbol for the next iteration
		prev = symbol
	}

	return result
}

func main() {
	// Test the romanToInt function with some examples
	result := romanToInt("II")
	fmt.Println(result) // Output: 2

	result = romanToInt("XII")
	fmt.Println(result) // Output: 12

	result = romanToInt("XXVII")
	fmt.Println(result) // Output: 27

	result = romanToInt("IV")
	fmt.Println(result) // Output: 4

	result = romanToInt("IX")
	fmt.Println(result) // Output: 9

	result = romanToInt("XLVIII")
	fmt.Println(result) // Output: 48
}
