package main

import (
	"errors"
	"fmt"
	"log"
)

func main() {
	err := errors.New("It's a mistake")
	fmt.Println(err)
	log.Fatal(err)
}
