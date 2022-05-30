package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func doubleNumber(number int) int {
	return number * 25
}

func main() {
	fmt.Println("Enter an integer number, please: ")
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.TrimSpace(input)
	userNumber, err := strconv.Atoi(input)
	if err != nil {
		log.Fatal(err)
	}

	result := doubleNumber(userNumber)
	fmt.Println("The result of operation is:", result)
}
