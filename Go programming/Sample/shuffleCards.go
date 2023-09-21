package main

import (
	"fmt"
	"math/rand"
	"time"
)

// shuffle randomly shuffles a slice of strings.
// It takes a slice of cards as input and shuffles them using the Fisher-Yates algorithm.
func shuffle(cards []string) {
	// Create a new source with a specific seed based on the current time
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)

	// Iterate through the cards slice
	for i := range cards {
		// Generate a random number between 0 and the length of the cards slice
		randomNumber := r.Intn(len(cards))

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
