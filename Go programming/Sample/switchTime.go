package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	dow := rand.Intn(7) + 1
	// fmt.Printf("Dow: %d\n", dow)

	var result string
	switch dow {
	case 6:
		result = "Saturday"
	case 7:
		result = "Sunday"
	default:
		result = "It's working day!"
	}

	fmt.Println(result)
}
