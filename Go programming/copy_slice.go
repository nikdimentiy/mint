package main

import (
	"fmt"
)

func main() {
	// Create an underlying array with 5 elements
	underlyingArray := [5]string{"a", "b", "c", "d", "e"}

	// Create a slice that references a portion of the underlying array
	// Slice from index 2 (inclusive) to index 4 (exclusive)
	slice1 := underlyingArray[2:4]

	// Create a new slice with the same length as the underlying array
	// Copy the elements from the underlying array to the new slice
	slice2 := make([]string, len(underlyingArray))
	copy(slice2, underlyingArray[:])

	// Modify the first two elements of slice1
	slice1[0] = "hello"
	slice1[1] = "developer"

	// Print the contents of slice1
	fmt.Println(slice1) // Output: [hello developer]

	// Print the contents of slice2
	fmt.Println(slice2) // Output: [a b c d e]
}
