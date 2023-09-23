// This program demonstrates the use of slices in Go.

package main

import (
    "fmt"
)

func main() {
    // Create an underlying array.
    underlyingArray := [5]string{"a", "b", "c", "d", "e"}

    // Create a slice from the underlying array, starting at index 2 and ending at index 4 (exclusive).
    slice1 := underlyingArray[2:4]

    // Create a new slice with the same length as the underlying array.
    slice2 := make([]string, len(underlyingArray))

    // Copy the elements of the underlying array to the new slice.
    len_array := copy(slice2, underlyingArray[:])

    // Modify the elements of the first slice.
    slice1[0] = "hello"
    slice1[1] = "developer"

    // Print the contents of the two slices and the copied length.
    fmt.Println(slice1) // Output: [hello developer]
    fmt.Println(slice2) // Output: [c d c d e]
    fmt.Println(len_array)
}
