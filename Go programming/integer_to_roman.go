// Preparation to coding interview: LeetCode task -> solution

package main

import "fmt"

// Define a function to convert an integer to its Roman numeral representation
func intToRoman(num int) string {
    // Initialize slices for Roman numeral symbols and their equivalent values
    symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

    // Initialize result string and index counter
    result := ""
    i := 0

    // Convert integer to Roman numeral symbols
    for num > 0 {
        for num >= values[i] {
            result += symbols[i] // Append the Roman numeral symbol
            num -= values[i]     // Subtract the current value from the input integer
        }
        i++ // Increment the index counter
    }

    // Return the Roman numeral representation of the input integer
    return result
}

func main() {
    // Test the function with sample inputs
    fmt.Println(intToRoman(3))      // Output: "III"
    fmt.Println(intToRoman(58))     // Output: "LVIII"
    fmt.Println(intToRoman(1994))   // Output: "MCMXCIV"
}
