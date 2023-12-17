package main

import (
	"fmt"     // import fmt package for formatted I/O
	"strings" // import strings package for string manipulation functions
)

const (
	_  = iota             // ignore first value by assigning to blank identifier
	KB = 1 << (10 * iota) // 1KB = 1024 bytes
	MB                    // 1MB = 1024 KB
	GB                    // 1GB = 1024 MB
	TB                    // 1TB = 1024 GB
	PB                    // 1PB = 1024 TB
	EB                    // 1EB = 1024 PB
	ZB                    // 1ZB = 1024 EB
	YB                    // 1YB = 1024 ZB
)

func main() {
	var fileSize float64 // declare variable to hold file size
	var unit string      // declare variable to hold unit

	// Get user input for file size and unit
	fmt.Print("Enter file size: ")
	fmt.Scan(&fileSize)

	fmt.Print("Enter unit (KB, MB, GB, TB): ")
	fmt.Scan(&unit)

	// Convert file size to bytes based on unit
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

	// Print the result in GB
	fmt.Printf("File size: %.2fGB\n", fileSize/GB)
}
