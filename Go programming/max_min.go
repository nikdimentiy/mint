package main

import (
    "fmt"       // Importing the fmt package for formatted I/O
    "os"        // Importing the os package to use command line arguments and exit the program
    "strconv"   // Importing the strconv package to convert strings to floats
)

// The main function is the entry point of the program
func main() {
    // os.Args holds the command line arguments, the first one is the program name
    arguments := os.Args

    // Check if at least one argument is provided (excluding the program name)
    if len(arguments) < 2 {
        fmt.Println("Please provide one or more floats.")
        os.Exit(1) // Exit the program with status code 1 indicating an error
    }

    // Try to convert the first argument to a float64, assuming it as both min and max initially
    min, err := strconv.ParseFloat(arguments[1], 64)
    if err != nil {
        fmt.Println("Error parsing float:", err) // Print the error if conversion fails
        os.Exit(1) // Exit the program with status code 1 indicating an error
    }
    max := min // Set max to the same value as min initially

    // Iterate over the remaining arguments starting from the second one
    for _, arg := range arguments[2:] {
        num, err := strconv.ParseFloat(arg, 64) // Convert each argument to float64
        if err != nil {
            fmt.Println("Error parsing float:", err) // Print the error if conversion fails
            os.Exit(1) // Exit the program with status code 1 indicating an error
        }
        // Update min and max if the current number is smaller or larger, respectively
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }

    // Print the minimum and maximum values found
    fmt.Println("Minimum:", min)
    fmt.Println("Maximum:", max)
}
