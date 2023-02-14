package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Enter the integer limit of operation: ")
	var total int
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.TrimSpace(input)
	limit, err := strconv.Atoi(input)
	if err != nil {
		log.Fatal(err)
	}

	for i := 0; i <= limit; i++ {
		total += i
	}
	fmt.Println(total)
}
