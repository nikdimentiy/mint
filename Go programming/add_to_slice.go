package main
/*

This program demonstrates the use of slices in Go to store and manipulate subscriber information.
It's program demo: How to add different data types in string slice.

It declares a slice of strings to store the subscribers and performs the following operations:
1. Appends the string "Aman" to the slice.
2. Appends the string "4.99" to the slice, formatted as a float with two decimal places.
3. Appends the string "true" to the slice, formatted as a Boolean.
4. Prints the slice of subscribers to the console.

Author: D.Nikey
Date: 09/17/23
*/


import "fmt"

func main() {
	// Declare a slice of strings to store the subscribers.
	subscriber := []string{}

	// Append the string "Aman" to the slice.
	subscriber = append(subscriber, "Aman")

	// Append the string "4.99" to the slice, formatted as a float with two decimal places.
	subscriber = append(subscriber, fmt.Sprintf("%.2f", 4.99))

	// Append the string "true" to the slice, formatted as a Boolean.
	subscriber = append(subscriber, fmt.Sprintf("%t", true))

	// Print the slice of subscribers to the console.
	fmt.Println(subscriber)
}
