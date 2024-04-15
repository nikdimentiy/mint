package main

import (
	"errors" // Importing the errors package to handle errors
	"fmt"    // Importing the fmt package for formatted I/O
	"os"     // Importing the os package to use operating system functionality
	"strconv" // Importing the strconv package for string conversion
)

// The main function is the entry point of the program
func main() {
	// Check if at least one argument is passed
	if len(os.Args) == 1 {
		fmt.Println("Please give one or more floats.")
		os.Exit(1) // Exit the program if no arguments are provided
	}

	arguments := os.Args // Retrieve the arguments passed to the program
	var min, max float64 // Declare variables to store the minimum and maximum values
	var n float64        // Declare a variable to store the current number being checked
	var err error = errors.New("An error") // Initialize an error variable with a default error

	k := 1 // Start from the second argument (index 1), as the first is the program name
	// Loop to find the first valid float argument
	for err != nil {
		if k >= len(arguments) {
			fmt.Println("None of the arguments is a float!")
			return // Exit the function if no valid float is found
		}
		// Try to convert the argument to a float64
		n, err = strconv.ParseFloat(arguments[k], 64)
		k++ // Move to the next argument
	}

	min = n // Set the first valid float as the initial minimum
	max = n // Set the first valid float as the initial maximum

	// Loop through the rest of the arguments starting from the third
	for i := 2; i < len(arguments); i++ {
		// Try to convert the argument to a float64
		n, err := strconv.ParseFloat(arguments[i], 64)
		if err == nil { // If conversion is successful
			if n < min { // Check if the current number is less than the current minimum
				min = n // Update the minimum
			}
			if n > max { // Check if the current number is greater than the current maximum
				max = n // Update the maximum
			}
		}
	}

	// Print the minimum and maximum values
	fmt.Println("Minimum:", min)
	fmt.Println("Maximum:", max)
}
