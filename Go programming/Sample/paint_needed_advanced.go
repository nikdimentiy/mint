package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// handleError prints an error message along with the error details.
func handleError(message string, err error) {
	fmt.Printf("Error %s: %v\n", message, err)
}

// getUserInput prompts the user for input and returns a float64 value.
// It takes a prompt string as a parameter and returns the user input and any error that occurred.
func getUserInput(prompt string) (float64, error) {
	fmt.Print(prompt)
	reader := bufio.NewReader(os.Stdin)
	inputStr, err := reader.ReadString('\n')
	if err != nil {
		return 0, err
	}
	inputStr = strings.TrimSpace(inputStr)
	input, err := strconv.ParseFloat(inputStr, 64)
	return input, err
}

// calculateArea calculates the area of a rectangle.
// It takes the width and height as parameters and returns the calculated area.
func calculateArea(width, height float64) float64 {
	return width * height
}

// formatResult formats the area value and returns it as a string.
// It takes the area as a parameter and returns the formatted result.
func formatResult(area float64) string {
	return fmt.Sprintf("%.3f liters needed\n", area/10.0)
}

func main() {
	width, err := getUserInput("Enter the width: ")
	if err != nil {
		handleError("reading width", err)
		return
	}

	height, err := getUserInput("Enter the height: ")
	if err != nil {
		handleError("reading height", err)
		return
	}

	area := calculateArea(width, height)
	result := formatResult(area)
	fmt.Println(result)
}
