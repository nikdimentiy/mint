// Mini-game: you can guess the number -  for 6 attempts?

package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	seconds := time.Now().UnixMicro()
	rand.Seed(seconds)
	target := rand.Intn(100) + 1
	fmt.Println("I guees a magical number - from 1 to 100:")

	reader := bufio.NewReader(os.Stdin)

	succes := false

	for guesses := 0; guesses < 6; guesses++ {
		fmt.Println("You have", 6-guesses, "attempts! ")
		fmt.Println("Enter your number: ")
		input, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}

		input = strings.TrimSpace(input)

		guess, err := strconv.Atoi(input)
		if err != nil {
			log.Fatal(err)
		}

		if guess > target {
			fmt.Println("Your entered number is greater than guessed!")
		} else if guess < target {
			fmt.Println("Your entered number less than guessed!")
		} else {
			succes = true
			fmt.Println("Congradulation! You WIN!")
			break
		}
	}
	if !succes {
		fmt.Println("Sorry. Your attempts are over!.Guess number is:", target)
	}
}
