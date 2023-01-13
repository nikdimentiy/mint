package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("The random integer i range (50 - 100): ")
	// the rand.Seed() function is used to set a seed value to generate pseudo-random numbers
	rand.Seed(time.Now().UnixNano()) // seed to get different result every time
	// v := rand.Intn(max-min) + min    // range is min to max
	value := rand.Intn(100-50) + 50
	fmt.Println(value)
}
