package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  // Set of letters
	digitBytes  = "0123456789"                                            // Set of digits
	symbolBytes = "!@#$%^&*()_-+={}[]<>,.?/~"                             // Set of symbols
)

// generatePassword generates a random password of a specified length.
func generatePassword(length int) string {
	var characters []byte
	characters = append(characters, []byte(letterBytes)...)
	characters = append(characters, []byte(digitBytes)...)
	characters = append(characters, []byte(symbolBytes)...)

	rand.Seed(time.Now().UnixNano()) // Set the random seed based on the current time
	password := make([]byte, length)
	for i := 0; i < length; i++ {
		password[i] = characters[rand.Intn(len(characters))] // Choose a random character from the combined set
	}

	return string(password)
}

func main() {
	length := 8 // Default password length
	password := generatePassword(length)
	fmt.Println("Generated password:", password)
}
