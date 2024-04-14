package main

import "fmt"

func main() {
    // Create a map to simulate a set
    m := make(map[string]bool)

    // Example sets
    setA := []string{"foo", "bar", "baz"}
    setB := []string{"bar", "qux"}

    // Add elements from setA to the map
    for _, elem := range setA {
        m[elem] = true
    }

    // Remove elements from setB
    for _, elem := range setB {
        delete(m, elem)
    }

    // Extract unique elements back into a new slice
    result := make([]string, 0)
    for elem := range m {
        result = append(result, elem)
    }

    fmt.Printf("Set difference: %v\n", result)  // Output: [foo baz]
}
