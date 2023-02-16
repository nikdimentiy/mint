# Coursera assignment --> coding: snippets in Python, Java, Go

#  Write a program which prompts the user to enter a string. The program searches through the entered string for the characters ‘i’, ‘a’, and ‘n’.
#  The program should print “Found!” if the entered string starts with the character ‘i’, ends with the character ‘n’, and contains the character ‘a’.
#  The program should print “Not Found!” otherwise. The program should not be case-sensitive, so it does not matter if the characters are upper-case or lower-case.

# <--- Python code --->

# Prompt the user to enter a string
string = input("Enter a string: ")
# Convert the string to lower-case
string = string.lower()
# Check if the string starts with 'i', ends with 'n', and contains 'a'
if string.startswith("i") and string.endswith("n") and "a" in string:
    # Print "Found!" if the condition is true
    print("Found!")
else:
    # Print "Not Found!" otherwise
    print("Not Found!")

# <--- Java code --->

# // Import the Scanner class
# import java.util.Scanner;
# public class Main {
#     public static void main(String[] args) {
#         // Create a Scanner object to read the user input
#         Scanner scanner = new Scanner(System.in);
#         // Prompt the user to enter a string
#         System.out.print("Enter a string: ");
#         // Read the string from the user input
#         String string = scanner.nextLine();
#         // Close the scanner
#         scanner.close();
#         // Convert the string to lower-case
#         string = string.toLowerCase();
#         // Check if the string starts with 'i', ends with 'n', and contains 'a'
#         if (string.startsWith("i") && string.endsWith("n") && string.contains("a")) {
#             // Print "Found!" if the condition is true
#             System.out.println("Found!");
#         } else {
#             // Print "Not Found!" otherwise
#             System.out.println("Not Found!");
#         }
#     }
# }

# <--- Go code --->

# package main
# // Import the fmt and strings packages
# import (
# 	"fmt"
# 	"strings"
# )
# func main() {
# 	// Prompt the user to enter a string
# 	fmt.Print("Enter a string: ")
# 	// Declare a variable to store the string
# 	var string string
# 	// Read the string from the standard input
# 	fmt.Scanln(&string)
# 	// Convert the string to lower-case
# 	string = strings.ToLower(string)
# 	// Check if the string starts with 'i', ends with 'n', and contains 'a'
# 	if strings.HasPrefix(string, "i") && strings.HasSuffix(string, "n") && strings.Contains(string, "a") {
# 		// Print "Found!" if the condition is true
# 		fmt.Println("Found!")
# 	} else {
# 		// Print "Not Found!" otherwise
# 		fmt.Println("Not Found!")
# 	}
# }
