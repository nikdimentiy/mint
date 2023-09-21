package main

import (
	"fmt"
	"math/rand"
	"time"
)

// shuffle randomly shuffles a slice of strings.
// It takes a slice of cards as input and shuffles them using the Fisher-Yates algorithm.
func shuffle(cards []string) {
	rand.Seed(time.Now().UnixNano())

	// Iterate through the cards slice
	for i := range cards {
		// Generate a random number between 0 and the length of the cards slice
		randomNumber := rand.Intn(len(cards))

		// Swap the current card with the card at the random position
		cards[i], cards[randomNumber] = cards[randomNumber], cards[i]
	}
}

func main() {
	cards := []string{"Ace", "King", "Queen", "Jack", "10"}
	fmt.Println("Before shuffle:", cards)

	// Shuffle the cards
	shuffle(cards)
	fmt.Println("After shuffle:", cards)
}
