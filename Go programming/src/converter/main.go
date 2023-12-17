package main

import (
	"fmt"
	"strings"
)

const (
	_  = iota // ignore first value by assigning to blank identifier
	KB = 1 << (10 * iota)
	MB
	GB
	TB
	PB
	EB
	ZB
	YB
)

func main() {
	var fileSize float64
	var unit string

	// Get user input for file size and unit
	fmt.Print("Enter file size: ")
	fmt.Scan(&fileSize)

	fmt.Print("Enter unit (KB, MB, GB, TB): ")
	fmt.Scan(&unit)

	// Convert file size to bytes
	switch strings.ToUpper(unit) {
	case "KB":
		fileSize *= float64(KB)
	case "MB":
		fileSize *= float64(MB)
	case "GB":
		fileSize *= float64(GB)
	case "TB":
		fileSize *= float64(TB)
	default:
		fmt.Println("Invalid unit. Please enter KB, MB, GB, or TB.")
		return
	}

	// Print the result
	fmt.Printf("File size: %.2fGB\n", fileSize/GB)
}
